import os, textwrap

base = os.path.join(os.path.dirname(__file__), "docs")
files = [
"core_language/control_flow.md",
"core_language/functions.md",
"core_language/modules_packages.md",
"core_language/classes_oop.md",
"core_language/error_handling.md",
"stdlib/files_paths.md",
"stdlib/serialization.md",
"stdlib/dates_times.md",
"stdlib/concurrency_primitives.md",
"stdlib/async_io.md",
"stdlib/text_processing.md",
"stdlib/testing_debugging.md",
"third_party/data_science.md",
"third_party/web_apis.md",
"third_party/cli_tools.md",
"third_party/databases.md",
"third_party/devops.md",
"packaging/pyproject_toml.md",
"packaging/building.md",
"packaging/versioning.md",
"packaging/publishing.md",
"performance/timing.md",
"performance/profiling.md",
"performance/optimisation.md",
"concurrency/thread_safety.md",
"concurrency/multiprocessing.md",
"concurrency/advanced_asyncio.md",
"typing/gradual_typing.md",
"typing/advanced.md",
"typing/ci_integration.md",
"best_practices/pep8_formatting.md",
"best_practices/project_layout.md",
"best_practices/documentation.md",
"best_practices/security.md",
"tooling/git_workflow.md",
"tooling/ci_cd.md",
"tooling/containerisation.md",
"tooling/task_runners.md",
"appendices/cheatsheets.md",
"appendices/glossary.md",
"appendices/further_reading.md",
"appendices/license_contrib.md",
]

template = textwrap.dedent("""\
# {title}

> **Status** – placeholder chapter. Replace this file with full tutorial + reference + doctest examples.

## Overview

Write a beginner‑friendly tutorial for **{title}** here. Include:

* Conceptual explanation
* Code snippets (runnable, tested with `pytest --doctest-modules`)
* A **Reference** box with concise tables / signatures
* End‑of‑chapter **Exercises** (doctest blocks)

## Reference

| Item | Description |
|------|-------------|
| Example | Fill in key APIs, flags, or patterns |

## Exercises (doctest)

```python
>>> True
True
```
""")

for rel in files:
    path = os.path.join(base, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    title = os.path.splitext(os.path.basename(rel))[0].replace('_',' ').title()
    with open(path, "w", encoding="utf-8") as f:
        f.write(template.format(title=title))
print("Created", len(files), "placeholder chapters.")