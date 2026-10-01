# Python Handbook

Welcome to the **Python Handbook** – a single source of truth for learning and referencing Python from the very first line of code to production‑grade packaging, performance tuning, and modern async patterns.

--- 

## Who is this for?

* **Absolute beginners** – no prior programming experience required.
* **Intermediate developers** – deepen your knowledge of the standard library, tooling, and best practices.
* **Advanced engineers** – quick reference for typing, concurrency internals, and optimisation tricks.

--- 

## How to read

| Mode | Description |
|------|-------------|
| **Tutorial** | Follow the narrative from top to bottom; each chapter ends with *Exercises* you can run. |
| **Reference** | Jump to the *Reference* boxes (collapsible) for concise API tables, signatures, and gotchas. |
| **Executable** | Every code block is a doctest – run `pytest --doctest-modules docs/` to verify. |

--- 

## Getting started

1. [Install Python & tooling](getting_started/installation.md)
2. Run your [first program](getting_started/first_program.md)
3. Dive into [Core Language](core_language/syntax_basic_types.md)

--- 

## Contribute

Found a typo? Want a new section? Open a PR – all examples are tested automatically.

```bash
pip install -e .[dev]
pre-commit install
pytest --doctest-modules docs/
```

--- 

*Happy Pythoning!* 🚀

## Table of Contents

```{toctree}
:maxdepth: 2
:glob:

getting_started/*
core_language/*
stdlib/*
third_party/*
packaging/*
performance/*
concurrency/*
typing/*
best_practices/*
tooling/*
appendices/*
```