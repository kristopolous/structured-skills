# Structured Skills (ss)

A Tiny VM for LLM-Powered Programs.

## Usage

```bash
python3 -m ss.cli <script.ss>
```

## Features

- **Vibe Decoder:** Natural language friendly syntax.
- **VM:** Stack-based execution with local scoping and control flow.
- **Tools:** Built-in support for `read`, `write`, `append_to_file`, `list_files`, `add`, `sum`.
- **Inference:** Bounded LLM calls via the `infer` keyword.
- **Skills:** Reusable routines defined with `def`.

## Tests

The `tests/` directory contains sample data and scripts:
- `tests/test_extraction.ss`: Extracts locations from text files.
- `tests/test_math.ss`: Performs arithmetic on numbers read from files.

Run tests:
```bash
python3 -m ss.cli tests/test_extraction.ss
python3 -m ss.cli tests/test_math.ss
```
