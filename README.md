# amix21

A tiny Python sample project used for practicing the pull request workflow.

## Install

```bash
pip install -e .
```

## Usage

```python
from amix21 import greeting

print(greeting("World"))  # -> "Hello, World!"
```

`greeting()` raises `ValueError` when the name is empty or only whitespace.

## Development

Run the tests with:

```bash
pip install pytest
pytest
```
