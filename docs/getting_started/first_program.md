# Your First Program

Let's write, run, and test a tiny script.

## 1. Create the file

```bash
mkdir -p ~/python_handbook_demo
cd ~/python_handbook_demo
cat > hello.py <<'EOF'
#!/usr/bin/env python3
"""A tiny greeting program."""


def greet(name: str) -> str:
    """Return a friendly greeting."""
    return f"Hello, {name}!"


if __name__ == "__main__":
    import sys

    # Default to "World" if no argument given
    target = sys.argv[1] if len(sys.argv) > 1 else "World"
    print(greet(target))
EOF
```

## 2. Run it

```bash
python hello.py               # → Hello, World!
python hello.py Ada           # → Hello, Ada!
```

## 3. Make it executable (Unix‑like)

```bash
chmod +x hello.py
./hello.py Grace              # → Hello, Grace!
```

## 4. Verify with **doctest** (runs automatically in CI)

```python
>>> from hello import greet
>>> greet("Test")
'Hello, Test!'
```

Run the test suite:

```bash
pytest --doctest-modules hello.py
```

You should see `1 passed`.

## 5. Add a simple **type‑check**

```bash
mypy hello.py
# Success: no issues found in 1 source file
```

## 6. Format & lint

```bash
ruff format hello.py
ruff check hello.py
```

Both should exit cleanly.

--- 

## Reference

| Concept | Snippet |
|---------|---------|
| Shebang | `#!/usr/bin/env python3` |
| Module guard | `if __name__ == "__main__":` |
| Argument parsing (stdlib) | `import sys; sys.argv` |
| Type hint (function) | `def greet(name: str) -> str:` |
| Docstring (PEP 257) | `"""Return a friendly greeting."""` |
| f‑string (3.6+) | `f"Hello, {name}!"` |

--- 

## Exercises

1. Extend `greet` to accept an optional `title` (e.g., `"Dr."`) and include it.
2. Add a second function `farewell(name: str) -> str` and call it when a `--bye` flag is present.
3. Write a **unit test** with `pytest` (not doctest) for both functions.