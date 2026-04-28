# Python for Data Science

The Python piscine is a project designed to introduce students to different concepts of the Python programming language, from simple built-in types manipulation to object-oriented programming (OOP).


## 📚 Overview

### 0 - Starting

This module contains a set of exercises to learn the basics of Python,
from simple syntax to package creation and project structure.


| Exercise | Description |
|----------|------------|
| ex00 | Variable assignment and basic printing |
| ex01 | Time module and formatted output |
| ex02 | Function definition |
| ex03 | Null checking |
| ex04 | Assertions |
| ex05 | Program entry point |
| ex06 | List comprehension and iterators |
| ex07 | Dictionaries |
| ex08 | `yield` |
| ex09 | Package creation |


---
### 1 - Array

This module contains a set of exercises to learn the basics of array manipulation.

| Exercise | Description |
|----------|-------------|
| ex00 | List manipulation |
| ex01 | 2D array slicing |
| ex02 | Image to NumPy array |
| ex03 | 2D array plotting |
| ex04 | 2D array transposition |
| ex05 | 3D array basic operations |


---
### 2 - DataTable

This module contains a set of exercises to learn the basics of pandas DataFrame manipulation and data visualization.

| Exercise | Description |
|----------|-------------|
| ex00 | CSV file loading |
| ex01 | DataFrame slicing and line plotting |
| ex02 | DataFrame value mapping and multi-column plotting |
| ex03 | DataFrame merging and scatter plotting |


---
### 3 - Oriented Object Programming

This module contains a set of exercises to learn the basics of classes, inheritance, and special methods.

| Exercise | Description |
|----------|-------------|
| ex00 | Abstract class and inheritance |
| ex01 | `__str__`, `__repr__` and `@classmethod` |
| ex02 | Diamond inheritance |
| ex03 | Operator overloading |
| ex04 | `@staticmethod` |


---
### 4 - Data Oriented Design

This module contains a set of exercises to learn function, decorators and class implementation for basic data description.

| Exercise | Description |
|----------|-------------|
| ex00 | Functions for statistics |
| ex01 | `nonlocal` keyword |
| ex02 | Decorators |
| ex03 | `@dataclass` |

## ⚙️ Setup

**<ins>Option 1:</ins>** Using `uv`
```bash
# Install uv (if not already installed)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Create a virtual environment and install dependencies from pyproject.toml
uv sync

# Activate the virtual environment
source .venv/bin/activate
```

**<ins>Option 2:</ins>** Using `pip` and `venv`:
```bash
# Create a virtual environment in the current directory
python3 -m venv .venv

# Activate the virtual environment
source .venv/bin/activate

# Install dependencies from pyproject.toml
python3 -m pip install -r requirements.txt

```

This will create and activate a ready-to-use Python virtual environment with
all required dependencies.


**<ins>At the end, run:</ins>**
```bash
# Deactivate the actual virtual environment
deactivate
```


## ▶️ How to run
```bash
python3 <file>.py
```