# FastAPI Lifespan Example

This project demonstrates the use of **FastAPI's new `lifespan` async context manager** feature (introduced in newer versions of FastAPI) to manage application startup and shutdown tasks.

## Why `lifespan`?
Previously, FastAPI used `@app.on_event("startup")` and `@app.on_event("shutdown")`.  
The new `lifespan` context manager is cleaner and colocates setup/teardown logic:

- **Before `yield`** → startup code (e.g., database setup).  
- **After `yield`** → shutdown code (e.g., cleanup, closing connections).  

This improves readability, reliability, and resource management.

## What this code does
- Configures an **SQLite async database** with SQLAlchemy.  
- Creates a `lifespan` context manager that:
  - **On startup**: creates database tables.  
  - **On shutdown**: disposes of the database engine.  
- Implements two API endpoints:
  - `POST /items/` → add new items.  
  - `GET /items/` → retrieve items.  
- Includes a health-check route `GET /`.

## Running the project
Install dependencies:
```bash
pip install "fastapi[all]" sqlalchemy aiosqlite


Reflection

I chose to implement the new lifespan feature in FastAPI because it reflects modern best practices for resource management.
This approach is cleaner than old event handlers and ensures setup/teardown logic lives in the same function.
In this project, I used it for database initialization and cleanup — but the same pattern works for caching, ML models, or any other resource-heavy tasks.
