
from contextlib import asynccontextmanager
from typing import AsyncGenerator, List

from fastapi import Depends, FastAPI
from sqlalchemy import select
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from pydantic import BaseModel

# 1. Database Configuration
DATABASE_URL = "sqlite+aiosqlite:///./test.db"

# Create the async engine
engine = create_async_engine(DATABASE_URL, echo=False)

# Create a session maker
async_session_factory = async_sessionmaker(engine, expire_on_commit=False)

# 2. SQLAlchemy Model (for the database table)
class Base(DeclarativeBase):
    pass

class Item(Base):
    __tablename__ = "items"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(index=True)
    description: Mapped[str | None] = mapped_column(default=None)

# 3. Pydantic Model (for API request/response)
class ItemCreate(BaseModel):
    name: str
    description: str | None = None

class ItemRead(BaseModel):
    id: int
    name: str
    description: str | None = None

    class Config:
        orm_mode = True

# 4. The Lifespan Context Manager
@asynccontextmanager
async def lifespan(app: FastAPI):
    # --- Startup ---
    print("Lifespan: Startup event")
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    print("Database tables created.")

    yield  # The app runs here

    # --- Shutdown ---
    print("Lifespan: Shutdown event")
    await engine.dispose()
    print("Database engine disposed.")

# 5. Create the FastAPI app with the lifespan manager
app = FastAPI(lifespan=lifespan)

# 6. Dependency to get a database session
async def get_db_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_factory() as session:
        yield session

# 7. API Routes
@app.post("/items/", response_model=ItemRead)
async def create_item(
    item_data: ItemCreate,
    session: AsyncSession = Depends(get_db_session)
):
    db_item = Item(name=item_data.name, description=item_data.description)
    session.add(db_item)
    await session.commit()
    await session.refresh(db_item)
    return db_item

@app.get("/items/", response_model=List[ItemRead])
async def read_items(
    skip: int = 0,
    limit: int = 100,
    session: AsyncSession = Depends(get_db_session)
):
    result = await session.execute(select(Item).offset(skip).limit(limit))
    items = result.scalars().all()
    return items

# Health check root endpoint
@app.get("/")
def read_root():
    return {"Hello": "World"}

