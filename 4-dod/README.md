# Python for Data Science – Data Oriented Design

This module contains a set of exercises to learn function, decorators and class implementation for data analysis.


## 📚 Overview

Each exercise focuses on a core concept:

| Exercise | Description |
|----------|-------------|
| ex00 | Functions for statistics |
| ex01 | `nonlocal` keyword |
| ex02 | Decorators |
| ex03 | `@dataclass` |

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