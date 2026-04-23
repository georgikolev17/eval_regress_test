# Tiny Intentionally Buggy Python Demo

This repository is a **minimal, intentionally buggy** project meant for testing AI bug-fixing evaluation harnesses.

## Contents

- `app.py`: application code with 8 small independent bugs.
- `test_app.py`: one pytest test per bug.
- `issues.md`: issue-style descriptions for each bug.
- `mapping.md`: issue-to-function-to-test mapping.
- `task_prompts.md`: one short fix prompt per issue.
- `initial_test_output.txt`: baseline failing pytest output.

## Run tests

```bash
pytest -q
```
