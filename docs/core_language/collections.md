# Collections

Python ships with four core container types plus a few specialised ones in `collections` and `typing`.

--- 

## 1. `list` – mutable sequence

```python
>>> fruits = ["apple", "banana", "cherry"]
>>> fruits.append("date")
>>> fruits[1] = "blueberry"
>>> fruits
['apple', 'blueberry', 'cherry', 'date']
```

**Common operations**

| Op | Example | Result |
|----|---------|--------|
| Index | `fruits[0]` | `'apple'` |
| Slice | `fruits[1:3]` | `['blueberry', 'cherry']` |
| Extend | `fruits += ["elderberry"]` | adds element |
| Pop | `fruits.pop()` | `'date'` (removes) |
| Sort (in‑place) | `fruits.sort()` | alphabetical |
| Reverse (in‑place) | `fruits.reverse()` | reversed order |

**List comprehensions**

```python
>>> [x**2 for x in range(5) if x % 2 == 0]
[0, 4, 16]
```

--- 

## 2. `tuple` – immutable sequence

```python
>>> point = (3.0, 4.0)
>>> x, y = point          # unpacking
>>> point[0] = 1          # TypeError
```

* Use for fixed‑size heterogeneous records (e.g., DB rows).
* Named tuples (`collections.namedtuple`, `typing.NamedTuple`) give field names.

```python
from typing import NamedTuple

class Point(NamedTuple):
    x: float
    y: float

p = Point(1.0, 2.0)
p.x, p.y   # (1.0, 2.0)
```

--- 

## 3. `set` – unordered unique collection

```python
>>> primes = {2, 3, 5, 7}
>>> primes.add(11)
>>> primes | {13, 17}          # union
{2, 3, 5, 7, 11, 13, 17}
>>> primes & {3, 5, 11}        # intersection
{3, 5, 11}
>>> primes - {2, 3}            # difference
{5, 7, 11}
```

* `frozenset` – immutable, hashable → can be dict key or set element.

--- 

## 4. `dict` – key/value mapping (hash table)

```python
>>> capitals = {"France": "Paris", "Japan": "Tokyo"}
>>> capitals["Germany"] = "Berlin"
>>> capitals.get("Italy", "Unknown")
'Unknown'
>>> for k, v in capitals.items():
...     print(k, "→", v)
France → Paris
Japan → Tokyo
Germany → Berlin
```

**Dict comprehensions**

```python
>>> {n: n**2 for n in range(5)}
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

**Merging (3.9+)**

```python
>>> a = {"x": 1}
>>> b = {"y": 2}
>>> a | b
{'x': 1, 'y': 2}
>>> a |= b
>>> a
{'x': 1, 'y': 2}
```

--- 

## 5. Specialised containers (`collections`)

| Class | Use‑case |
|-------|----------|
| `Counter` | Multiset / frequency table |
| `defaultdict` | Auto‑create missing values |
| `OrderedDict` | Preserve insertion order (dict does since 3.7) |
| `deque` | Fast appends/pops both ends |
| `ChainMap` | Layer multiple dicts |
| `namedtuple` | Lightweight immutable record |

```python
from collections import Counter, defaultdict, deque

cnt = Counter("abracadabra")
cnt.most_common(2)          # [('a', 5), ('b', 2)]

dd = defaultdict(list)
dd["key"].append(1)         # no KeyError

dq = deque([1, 2, 3])
dq.appendleft(0)            # deque([0, 1, 2, 3])
```

--- 

## 6. Reference – Complexity cheat‑sheet (average case)

| Operation | list | tuple | set | dict |
|-----------|------|-------|-----|------|
| Index / key access | O(1) | O(1) | — | O(1) |
| Append / add | O(1) amort. | — | O(1) | O(1) |
| Pop last | O(1) | — | — | — |
| Pop arbitrary | O(n) | — | O(1) | O(1) |
| Membership (`in`) | O(n) | O(n) | O(1) | O(1) (keys) |
| Iteration | O(n) | O(n) | O(n) | O(n) |

--- 

## Exercises (doctest)

```python
>>> [c for c in "hello" if c not in "aeiou"]
['h', 'l', 'l']
>>> {i: i**3 for i in range(3)}
{0: 0, 1: 1, 2: 8}
>>> from collections import Counter
>>> Counter("mississippi")["s"]
4
```

--- 

## Further reading

* **PEP 584** – Union operators for `dict`
* **docs.python.org** – `collections` module reference
* **Effective Python** Item 14: “Prefer `list` comprehensions over `map`/`filter`”