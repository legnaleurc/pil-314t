# PIL.Image Import Test (uv)

This project demonstrates the potential crash when importing `PIL.Image` in Python 3.14t (free-threaded).

## Requirements

- Python 3.14 or later
- uv

## Setup

```bash
uv sync --dev
```

## Run Tests

```bash
uv run pytest tests/ -v
```

## GitHub Actions

The project includes a GitHub Actions workflow that automatically tests the import on Python 3.14t (free-threaded).

## Expected Behavior

When running on Python 3.14t with free-threading enabled, importing `PIL.Image` may cause a crash or segmentation fault.
