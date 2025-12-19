# PIL.Image Python 3.14t Crash Demonstration

This repository contains two identical test projects that demonstrate a crash when importing `PIL.Image` in Python 3.14t (free-threaded version).

## Projects

### poetry-project
Uses **Poetry 2.2** for dependency management.

### uv-project
Uses **uv** for dependency management.

## Structure

Both projects contain:
- `pyproject.toml` - Project configuration with Python 3.14+ requirement and latest Pillow
- `tests/test_pil_import.py` - Test that imports PIL.Image
- `.github/workflows/test.yml` - GitHub Actions workflow to run tests on Python 3.14t

## Expected Behavior

When running the tests on Python 3.14t (free-threaded), the import of `PIL.Image` may cause a crash or segmentation fault, demonstrating compatibility issues with the free-threaded Python implementation.

## Running Locally

### Poetry Project
```bash
cd poetry-project
poetry install --with dev
poetry run pytest tests/ -v
```

### uv Project
```bash
cd uv-project
uv sync --dev
uv run pytest tests/ -v
```

## GitHub Actions

Both projects include GitHub Actions workflows that will automatically run tests on Python 3.14t when code is pushed or pull requests are created.
