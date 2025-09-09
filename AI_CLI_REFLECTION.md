
# AI CLI Exploration – Gemini CLI

## Goal
Explore an AI-powered CLI tool (Gemini CLI) by running commands on my Python project, refactoring code, adding a new feature, and reflecting on its usefulness.

---

## Commands and Outputs

### 1. Refactor
Command:
```bash
gemini -p "Refactor this code" < alx_be_python/python_introduction/rectangle_area.py

Output (summary):

Gemini encapsulated the area calculation in a reusable function calculate_area(length, width).

It replaced inline multiplication with a function call.

Suggested best practices like code organization and reusability.

Refactored code suggested:

def calculate_area(length, width):
  """Calculates the area of a rectangle."""
  return length * width

length = 10
width = 5

area = calculate_area(length, width)

print(f"The area of the rectangle is: {area}")

Explain

Command:

gemini -p "Explain what this script does in plain English" < alx_be_python/rectangle_area.py


Output (summary):

The script calculates the area of a rectangle.

It assigns length = 10 and width = 5.

Multiplies them to get the area (50) and prints it.


Explain

Command:gemini -p "Explain what this script does in plain English" < alx_be_python/rectangle_area.py

Output (summary):

The script calculates the area of a rectangle.

It assigns length = 10 and width = 5.

Multiplies them to get the area (50) and prints it.

New Feature

Command:gemini -p "Modify this script so it also calculates the perimeter of the rectangle" < alx_be_python/rectangle_area.py



length = 10
width = 5

area = length * width
perimeter = 2 * (length + width)

print(f"The area of the rectangle is: {area}")
print(f"The perimeter of the rectangle is: {perimeter}")


Reflection

Using Gemini CLI inside my Python project was very insightful:

Code Quality – The refactoring step improved the readability of my Python script by introducing a function and better structure.

Documentation – The explanation step showed how AI can describe code in plain English, which is helpful for beginners or for quick documentation.

Feature Development – The new feature prompt demonstrated how AI can assist in adding new logic (perimeter calculation) quickly.

Importance of AI CLI Tools

AI-powered CLI tools like Gemini CLI are valuable because they:

Integrate directly into the developer workflow without leaving the terminal.

Speed up debugging, refactoring, and feature ideation.

Act like a coding partner, not a replacement, enhancing productivity and learning

