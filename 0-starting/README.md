# Python for Data Science – Starting

This module contains a set of exercises to learn the basics of Python,
from simple syntax to package creation and project structure.

-----

## 📚 Overview

Each exercise focuses on a core concept:

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


## 🚀 Setup

1) Install uv (if not already)
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

2) At the root of the project, run:
```bash
# Create the virtual environment from pyproject.toml
uv sync

# Activate the virtual environment
source .venv/bin/activate
```
This will create and activate a ready-to-use Python virtual environment with
all required dependencies.

3) At the end, run:
```bash
deactivate
```
This will deactivate the virtual environment.


## ▶️ How to run
```bash
python3 <file>.py
```