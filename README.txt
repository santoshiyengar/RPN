1) pip install pytest
2) cd path_to_rpn
3) python rpn_main.py
4) py.test
5) To run in debug mode and print all run py.test -v -s


Test Results:
=============================================================== test session starts ================================================================
platform darwin -- Python 2.7.5, pytest-3.0.5, py-1.4.32, pluggy-0.4.0 -- /usr/bin/python
cachedir: .cache
rootdir: /Users/santoshi/Projects/rpn, inifile: 
collected 22 items 

tests/test_rpn.py::test_binary_operator_exists PASSED
tests/test_rpn.py::test_binary_operator_values PASSED
tests/test_rpn.py::test_unary_operator_exists PASSED
tests/test_rpn.py::test_unary_operator_value PASSED
tests/test_rpn.py::test_get_input_help_with_h PASSED
tests/test_rpn.py::test_get_input_help PASSED
tests/test_rpn.py::test_get_input_quit_with_q PASSED
tests/test_rpn.py::test_get_input_quit PASSED
tests/test_rpn.py::test_rpn_help_text_file PASSED
tests/test_rpn.py::test_rpn_help_contents PASSED
tests/test_rpn.py::test_is_expression_with_None PASSED
tests/test_rpn.py::test_is_expression_for_help PASSED
tests/test_rpn.py::test_is_expression_for_quit PASSED
tests/test_rpn.py::test_evaluate_valid_expressions Output is 1 for 50 % 2 *
Output is 4 for 6 2 * 3 /
Output is 24 for 12 3 / !
Output is 14 for 5 1 2 + 4 * + 3 -
Output is 26 for 3 ! 4 5 * +
Output is 17 for 2 3 ^ 4 5 + +
Output is -4 for 1 2 3 + -
PASSED
tests/test_rpn.py::test_evaluate_invalid_expressions Output is error : Not enough Operands to proceed with unary operation for !
Output is error : Not a Valid RPN, try until you succeed...e.g. 2 3 + for 2 3 4 +
Output is error : Not enough Operands to proceed with binary operation for 2 +
Output is error : Not enough Operands to proceed with unary operation for %
Output is error : Not a Valid RPN, try until you succeed...e.g. 2 3 + for 6sad
PASSED
tests/test_rpn_error.py::test_get_error_message PASSED
tests/test_rpn_error.py::test_get_error_message_binary_operation PASSED
tests/test_rpn_error.py::test_get_error_message_unary_operation PASSED
tests/test_rpn_error.py::test_existence_error_dictionary PASSED
tests/test_rpn_main.py::test_main PASSED
tests/test_rpn_math.py::test_rpn_math_percentage PASSED
tests/test_rpn_math.py::test_rpn_math_is_valid_number PASSED

============================================================ 22 passed in 0.05 seconds =============================================================
