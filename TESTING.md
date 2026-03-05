# Testing Strategy — Quick-Calc

This document describes the testing approach used for Quick-Calc, explains the decisions behind what was and was not tested, and maps the strategy to the core concepts covered in the module lecture.

---

## 1. Testing Strategy Overview

The test suite is divided into two layers:

- **Unit tests** (`tests/test_unit.py`) — 15 tests that verify each method of the `Calculator` class in complete isolation.
- **Integration tests** (`tests/test_integration.py`) — 6 tests that simulate realistic end-to-end user interactions through the CLI (`main.py`), verifying that the input/output layer and the core logic interact correctly.

### What was tested

- All four arithmetic operations (add, subtract, multiply, divide).
- The clear/reset function.
- Edge cases: division by zero, negative numbers, decimal numbers, very large numbers, multiplication by zero.
- End-to-end CLI flows: selecting a menu option, entering numbers, and receiving the correct result.
- The CLI's graceful error handling for division by zero.

### What was not tested and why

- **Performance / Non-functional testing**: The application performs single arithmetic operations whose execution time is negligible. Load or stress testing would add no meaningful value at this scale.
- **UI/display formatting**: The exact whitespace or cosmetic layout of the CLI menu was not asserted on. Display formatting is presentation detail, not logic, and is likely to change without affecting correctness.
- **Persistence**: Quick-Calc holds no state between sessions and writes no files, so there is nothing to test around data persistence.
- **Concurrency**: The application is single-threaded and has no concurrency concern.

---

## 2. Lecture Concepts Applied

### 2.1 The Testing Pyramid

The Testing Pyramid recommends having many unit tests at the base, fewer integration tests in the middle, and even fewer end-to-end/UI tests at the top. This suite follows that shape:

| Layer       | Count | Proportion |
|-------------|-------|------------|
| Unit        | 15    | ~71%       |
| Integration | 6     | ~29%       |
| E2E / UI    | 0     | 0%         |

Unit tests are fast, isolated, and cheap to write and maintain, so they form the bulk of the suite. Integration tests are fewer but verify real interaction paths. No browser or GUI E2E layer exists because the application is CLI-only and the integration tests already cover full user journeys.

### 2.2 Black-box vs White-box Testing

**Unit tests** were written using a **white-box** approach: the internal structure of `calculator.py` was known during test design. Tests directly exercise each method, cover known branches (e.g., the `if b == 0` guard in `divide`), and verify internal state (e.g., `calc.result` after `clear()`). This is possible because the author wrote both the code and the tests.

**Integration tests** were written using a **black-box** approach: `main()` is treated as a black box. The tests supply stdin inputs and inspect stdout outputs without any knowledge of how `main()` internally routes those inputs to the `Calculator` methods. This mirrors a real user's perspective — they interact through the interface and observe the result.

### 2.3 Functional vs Non-Functional Testing

All tests in this suite are **functional tests** — they verify that the software does what it is specified to do (correct arithmetic results, graceful error messages, successful reset). Non-functional qualities such as performance, usability, security, and reliability were explicitly out of scope for this iteration. Quick-Calc's specification (Section 2 of the assignment) defines only functional requirements, so no non-functional test coverage was needed.

### 2.4 Regression Testing

The test suite is designed to act as a **regression guard** for all future changes. Every core behaviour of `Calculator` is covered by at least one unit test, so any future refactoring that accidentally breaks arithmetic logic (e.g., an off-by-one error, a sign flip, or a missing zero-guard) will immediately surface as a failing test when `pytest` is run. The integration tests additionally catch regressions in the CLI routing layer — for example, if a future developer accidentally swaps the "Add" and "Subtract" menu options, `test_full_subtraction_sequence` would fail.

Running `pytest tests/ -v` before every merge or release is the recommended practice to prevent regressions from reaching production.

---

## 3. Test Results Summary

The table below reflects the results of running `pytest tests/ -v` after the initial implementation was complete.

| Test Name                                    | File                  | Type        | Status |
|----------------------------------------------|-----------------------|-------------|--------|
| test_add_two_positive_integers               | test_unit.py          | Unit        | PASS   |
| test_add_negative_numbers                    | test_unit.py          | Unit        | PASS   |
| test_add_positive_and_negative               | test_unit.py          | Unit        | PASS   |
| test_subtract_basic                          | test_unit.py          | Unit        | PASS   |
| test_subtract_producing_negative_result      | test_unit.py          | Unit        | PASS   |
| test_multiply_two_positive_integers          | test_unit.py          | Unit        | PASS   |
| test_multiply_by_zero                        | test_unit.py          | Unit        | PASS   |
| test_multiply_decimal_numbers                | test_unit.py          | Unit        | PASS   |
| test_divide_basic                            | test_unit.py          | Unit        | PASS   |
| test_divide_produces_decimal                 | test_unit.py          | Unit        | PASS   |
| test_divide_by_zero_raises_error             | test_unit.py          | Unit        | PASS   |
| test_add_very_large_numbers                  | test_unit.py          | Unit        | PASS   |
| test_subtract_decimal_numbers                | test_unit.py          | Unit        | PASS   |
| test_clear_resets_result_to_zero             | test_unit.py          | Unit        | PASS   |
| test_clear_returns_zero                      | test_unit.py          | Unit        | PASS   |
| test_full_addition_sequence                  | test_integration.py   | Integration | PASS   |
| test_full_subtraction_sequence               | test_integration.py   | Integration | PASS   |
| test_full_multiplication_sequence            | test_integration.py   | Integration | PASS   |
| test_full_division_sequence                  | test_integration.py   | Integration | PASS   |
| test_clear_resets_display_after_calculation  | test_integration.py   | Integration | PASS   |
| test_division_by_zero_shows_error_message    | test_integration.py   | Integration | PASS   |

**Total: 21 tests — 21 passed, 0 failed.**
