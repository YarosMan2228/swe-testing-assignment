# Testing Strategy — Quick-Calc

## What Was Tested

- All four operations: add, subtract, multiply, divide
- Clear/reset
- Edge cases: division by zero, negatives, decimals, large numbers
- Full CLI interactions from menu selection to result output

Didn't test performance or UI formatting — no point for an app this simple.

---

## Lecture Concepts

**Testing Pyramid** — most tests are unit tests (fast, isolated), fewer integration tests on top, no E2E layer needed.

| Layer       | Count |
|-------------|-------|
| Unit        | 15    |
| Integration | 6     |
| E2E         | 0     |

**Black-box vs White-box** — unit tests are white-box (we know the internals, test specific branches). Integration tests are black-box (feed inputs to the CLI, check what comes out).

**Functional vs Non-Functional** — all tests are functional. We check correct results and error handling, not performance or security.

**Regression Testing** — every operation is covered, so breaking something in the future will immediately show up as a failed test.

---

## Test Results

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

**21 tests — all passed.**
