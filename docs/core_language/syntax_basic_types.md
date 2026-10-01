# Syntax & Basic Types

> **Goal** – Understand the building blocks of every Python program.

--- 

## 1. Source file basics

| Rule | Example |
|------|---------|
| UTF‑8 encoding (default) | `# -*- coding: utf-8 -*-` (optional) |
| Statements end at newline (no `;`) | `x = 1` |
| Indentation = block structure (4 spaces) | `if True:\n    print("ok")` |
| Comments start with `#` | `# this is a comment` |
| Docstrings – first statement in module/function/class | `"""Module docstring."""` |

--- 

## 2. Numeric types

| Type | Literal examples | Notes |
|------|------------------|-------|
| `int` | `42`, `0b1010`, `0o52`, `0x2A` | Unlimited precision |
| `float` | `3.14`, `1e-3`, `2.5E4` | IEEE‑754 double |
| `complex` | `1+2j`, `3j` | `z.real`, `z.imag` |
| `bool` | `True`, `False` | Subclass of `int` (`True==1`) |

```python
>>> 3 + 4 * 2          # precedence
11
>>> 7 // 2, 7 % 2      # floor division, modulo
(3, 1)
>>> 2 ** 10            # power
1024
>>> 0.1 + 0.2          # floating‑point quirk
0.30000000000000004
```

--- 

## 3. Text – `str`

* Immutable sequence of Unicode code points.
* Literals: `'single'`, `"double"`, `'''triple'''`, `"""triple"""`.
* Escape sequences: `\n`, `\t`, `\uXXXX`, `\UXXXXXXXX`.

```python
>>> "hello" + " " + "world"
'hello world'
>>> f"{2**10 = }"          # debug f‑string (3.8+)
'2**10 = 1024'
>>> "café".encode("utf-8")
b'caf\xc3\xa9'
```

Common methods (all return new strings):

| Method | Purpose |
|--------|---------|
| `str.lower()`, `upper()`, `casefold()` | Case conversion |
| `strip()`, `lstrip()`, `rstrip()` | Trim whitespace |
| `split(sep)`, `rsplit()`, `splitlines()` | Split into list |
| `join(iterable)` | Concatenate with separator |
| `replace(old, new)` | Replace substrings |
| `startswith()/endswith()` | Prefix / suffix test |
| `format()` / f‑strings | Advanced formatting |

--- 

## 4. `bytes` & `bytearray`

```python
>>> b = b"binary"
>>> ba = bytearray(b)
>>> ba[0] = 0x42
>>> ba
bytearray(b'Binary')
```

* `bytes` – immutable; `bytearray` – mutable.
* Use `.decode(encoding)` / `.encode(encoding)`.

--- 

## 5. `None`

* Singleton representing *absence of value*.
* Default return of functions without explicit `return`.

```python
>>> def f(): pass
>>> f() is None
True
```

--- 

## 6. Built‑in constants

| Constant | Meaning |
|----------|---------|
| `True`, `False` | Boolean literals |
| `None` | Null value |
| `Ellipsis` (`...`) | Placeholder in slicing / type hints |
| `NotImplemented` | Returned by binary ops when unsupported |

--- 

## 7. Reference – Operator Precedence (high → low)

| Precedence | Operators |
|------------|-----------|
| 1 | `( )`, `[ ]`, `{ }`, `x.y`, `x[…]`, `x(...)` |
| 2 | `**` |
| 3 | `+x`, `-x`, `~x` |
| 4 | `*`, `@`, `/`, `//`, `%` |
| 5 | `+`, `-` |
| 6 | `<<`, `>>` |
| 7 | `&` |
| 8 | `^` |
| 9 | `|` |
|10| Comparisons (`in`, `not in`, `is`, `is not`, `<`, `<=`, `>`, `>=`, `!=`, `==`) |
|11| `not` |
|12| `and` |
|13| `or` |
|14| `if – else` (ternary) |
|15| `lambda` |
|16| `:=` (walrus) |

--- 

## Exercises (run with `pytest --doctest-modules`)

```python
>>> 2 ** 3 ** 2          # right‑associative **
512
>>> "abc" * 3
'abcabcabc'
>>> b"hello".decode()
'hello'
>>> None is None
True
```

--- 

## Further reading

* **PEP 3101** – Advanced string formatting
* **PEP 3112** – Tuple unpacking improvements
* **Real Python** – “Python Basics” series