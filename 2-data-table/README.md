# Python for Data Science – DataTable

This module contains a set of exercises to learn the basics of pandas DataFrame
manipulation and data visualization.

## 📚 Overview

Each exercise focuses on a core concept:

| Exercise | Description |
|----------|-------------|
| ex00 | CSV file loading |
| ex01 | DataFrame slicing and line plotting |
| ex02 | DataFrame value mapping and multi-column plotting |
| ex03 | DataFrame merging and scatter plotting |


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