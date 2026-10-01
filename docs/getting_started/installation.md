# Installing Python & Tooling

This chapter gets a **consistent, reproducible** Python environment on any OS.

## 1. Install a Python version manager

| Tool | Platform | Install command |
|------|----------|-----------------|
| **pyenv** | macOS / Linux | `brew install pyenv` / `curl https://pyenv.run \| bash` |
| **pyenv-win** | Windows | `git clone https://github.com/pyenv-win/pyenv-win.git %USERPROFILE%\.pyenv` |
| **conda / miniforge** | All | `winget install -e --id Miniforge3.Miniforge3` (Windows) / `brew install miniforge` (macOS) |

> **Tip** – `pyenv` lets you install multiple CPython versions side‑by‑side and set a per‑project version via `.python-version`.

## 2. Install the latest stable CPython

```bash
# List available versions
pyenv install --list | grep "^\s*3\.[0-9]*\.[0-9]*$" | tail -5

# Install (example 3.12.4)
pyenv install 3.12.4
pyenv global 3.12.4   # or `pyenv local 3.12.4` inside a project
```

Verify:

```bash
python --version   # → Python 3.12.4
python -m pip --version
```

## 3. Create an isolated virtual environment

```bash
python -m venv .venv          # creates .venv/ in current dir
source .venv/bin/activate     # Linux/macOS
.venv\Scripts\activate        # Windows (cmd)
.venv\Scripts\Activate.ps1    # Windows (PowerShell)
```

You should see `(.venv)` prefixed in your prompt.

## 4. Upgrade core packaging tools

```bash
python -m pip install --upgrade pip setuptools wheel
```

## 5. Recommended project‑level tooling (optional but encouraged)

| Tool | Purpose | Install |
|------|---------|---------|
| **poetry** | Dependency resolution, publishing, virtualenv management | `pipx install poetry` |
| **pipx** | Isolated CLI apps (e.g., `black`, `ruff`) | `pipx install pipx` |
| **pre-commit** | Git hooks for linting/formatting | `pipx install pre-commit` |
| **ruff** | Fast linter + formatter (replaces flake8 + black) | `pipx install ruff` |
| **mypy / pyright** | Static type checking | `pipx install mypy` / `pipx install pyright` |

> **Why `pipx`?** It installs each CLI in its own venv, avoiding version conflicts with your project.

## 6. Verify a fully‑working stack

```bash
python -c "import sys, json, pathlib; print(sys.version)"
python -m pytest --version
ruff --version
mypy --version
```

All commands should exit with `0` and print versions.

--- 

## Reference Cheat‑Sheet

```text
# pyenv basics
pyenv install <version>
pyenv global <version>
pyenv local <version>
pyenv versions
pyenv which python

# venv basics
python -m venv .venv
source .venv/bin/activate
deactivate

# poetry basics (if you adopt it)
poetry new myproj
poetry add requests
poetry lock
poetry build
poetry publish
```

--- 

## Exercises

1. Install **two** Python versions with `pyenv` and switch between them.
2. Create a venv, install `requests`, and run `python -c "import requests; print(requests.__version__)"`.
3. Add a `pre-commit` hook that runs `ruff check` and `ruff format` on every commit.