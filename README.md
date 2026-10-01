# Python Handbook

A comprehensive, beginner‑to‑advanced handbook covering core Python, the standard library, popular third‑party packages, testing, packaging, performance, concurrency, type hints, best practices, and project tooling.

**Formats**: Markdown (source), HTML (MkDocs Material), PDF (Sphinx + LaTeX)  
**Executable examples**: All code blocks are runnable via `pytest --doctest-modules`  
**License**: MIT (see LICENSE)

---

## Quick Start

```bash
# Clone and enter the repo
git clone https://github.com/yourname/python-handbook.git
cd python-handbook

# Create a virtual environment and install dev dependencies
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -e .[dev]
```

### Build the documentation

```bash
# HTML (MkDocs Material)
mkdocs serve          # live preview at http://localhost:8000
mkdocs build          # static site in ./site

# PDF (Sphinx)
cd docs/sphinx
make html
make latexpdf         # PDF in ./build/latex/python_handbook.pdf
```

### Run the test suite (verifies every example)

```bash
pytest --doctest-modules docs/
```

---

## Table of Contents (generated from `mkdocs.yml`)

See the sidebar in the HTML version or the PDF bookmarks.

---

## Contributing

1. Fork the repo
2. Create a feature branch (`git checkout -b my-topic`)
3. Write / update Markdown in `docs/` – keep examples runnable
4. Run `pytest --doctest-modules docs/` and `pre-commit run --all-files`
5. Open a Pull Request

---

## License

MIT © 2025 Your Name