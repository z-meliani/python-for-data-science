# Python for Data Science – Starting

This module contains a set of exercises to learn the basics of Python,
from simple syntax to package creation and project structure.


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

# Install dependencies from requirements.txt
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