# Quick-Calc

Quick-Calc is a lightweight command-line calculator application written in Python. It supports the four fundamental arithmetic operations — addition, subtraction, multiplication, and division — plus a clear/reset function. The project was built to demonstrate professional software development practices, including a structured testing strategy, semantic versioning, and conventional Git commit history.

---

## Features

| Operation      | Example          |
|----------------|------------------|
| Addition       | 5 + 3 = 8        |
| Subtraction    | 10 - 4 = 6       |
| Multiplication | 6 × 7 = 42       |
| Division       | 8 ÷ 2 = 4        |
| Clear (C)      | Resets result to 0 |

Division by zero is handled gracefully — the application displays a descriptive error message instead of crashing.

---

## Setup Instructions

### Prerequisites

- Python 3.8 or later
- pip

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the application

```bash
python main.py
```

Follow the on-screen menu to select an operation and enter numbers.

---

## How to Run Tests

All tests are written using **pytest** and can be executed with a single command from the project root:

```bash
pytest tests/ -v
```

To run only unit tests:

```bash
pytest tests/test_unit.py -v
```

To run only integration tests:

```bash
pytest tests/test_integration.py -v
```

A passing test run should report **0 failures** across all test files.

---

## Testing Framework Research

### Pytest vs Unittest — Comparative Analysis

Python ships with a built-in testing module called **unittest**, which is modelled after Java's JUnit. It requires tests to be organised inside classes that inherit from `unittest.TestCase`, and assertions are made through methods like `self.assertEqual()` and `self.assertRaises()`. This structure is explicit and familiar to developers with an object-oriented background, and it integrates seamlessly into the standard library without any additional installation. However, the boilerplate it demands — particularly for fixtures and parameterised tests — can make test files verbose and harder to read at a glance.

**Pytest** is a third-party framework that has become the de-facto standard for Python testing. It uses plain functions instead of classes, and its assertion introspection engine rewrites `assert` statements at collection time so that failures produce detailed, human-readable diffs without any custom message. Pytest's fixture system (using the `@pytest.fixture` decorator) is significantly more flexible and composable than `unittest`'s `setUp`/`tearDown` approach, supporting dependency injection, parameterisation with `@pytest.mark.parametrize`, and a rich plugin ecosystem (e.g., `pytest-cov` for coverage, `pytest-mock` for mocking).

For this project, **pytest** was chosen because it reduces boilerplate, produces clearer failure output, and scales well as the test suite grows. The fixture-based approach makes it straightforward to create isolated `Calculator` instances for every test without repeating setup code. The `pytest.approx` helper also simplifies assertions on floating-point results, which is critical for a calculator application.

---

## Project Structure

```
swe-testing-assignment/
├── calculator.py          # Core calculator logic
├── main.py                # CLI interface
├── tests/
│   ├── __init__.py
│   ├── test_unit.py       # Unit tests (15 tests)
│   └── test_integration.py# Integration tests (6 tests)
├── requirements.txt
├── .gitignore
├── README.md
└── TESTING.md
```

---

## Version History

See [Releases](../../releases) for the full changelog. The current stable release is **v1.0.0**.
