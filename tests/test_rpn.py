import operator
import math
import rpn
from rpn import RPN
from rpn_math import RPNMath


def test_binary_operator_exists():
    #ensuring the binary_operator dictionary exists.
    assert isinstance(RPN.binary_operators, dict)

def test_binary_operator_values():
    #ensuring the binary_operator dictionary values are right.
    assert RPN.binary_operators== {'+' : operator.add, '-' : operator.sub, '*' : operator.mul, '/' : operator.div, '^' : operator.pow,} 
    
def test_unary_operator_exists():    
    #ensuring the unary_operator dictionary exists.
    assert isinstance(RPN.binary_operators, dict)

def test_unary_operator_value():
    #ensuring the unary_operator dictionary exists.
    assert RPN.unary_operators=={ '!' : math.factorial, '%' : RPNMath.percentage}

#Input value Assertions
def test_get_input_help_with_h():
    rpn.raw_input = lambda _: 'h'
    text_input = RPN.get_input()
    assert text_input == 'h'

def test_get_input_help():
    rpn.raw_input = lambda _: 'help'
    text_input = RPN.get_input()
    assert text_input == 'help'

def test_get_input_quit_with_q():
    rpn.raw_input = lambda _: 'q'
    text_input = RPN.get_input()
    assert text_input == 'q'

def test_get_input_quit():
    rpn.raw_input = lambda _: 'quit'
    text_input = RPN.get_input()
    assert text_input == 'quit'

def test_is_expression_with_None():
    #Check if None passed, it returns True.
    assert RPN.is_expression(None) == True

def test_is_expression_with_empty_string():
    #Check if None passed, it returns True.
    assert RPN.is_expression('') == False

def test_is_expression_for_help():
    #Having this check for future Implementation.
    for help_text in ["h","help"]:
        assert help_text == help_text

def test_is_expression_for_quit():
    #Having this check for future Implementation.
    for quit_text in ["q","quit"]:
        assert quit_text == quit_text


def test_evaluate_valid_expressions():
    #Testing the positive Test cases
    test_io_cases={
                      "1 2 3 + -":-4,
                      "6 2 * 3 /":4,
                      "2 3 ^ 4 5 + +":17,
                      "50 % 2 *":1,
                      "3 ! 4 5 * +":26,
                      "12 3 / !":24,
                      "5 1 2 + 4 * + 3 -":14,
                  }
    for expression , expected_output in test_io_cases.iteritems():
        actual_op = RPN.evaluate_expression(expression)
        print "Output is %s for %s" % (expected_output,expression)
        assert   actual_op == expected_output

def test_evaluate_invalid_expressions():
    #Testing the Negative Test cases
    test_io_cases={
                      "2 +":"error : Not enough Operands to proceed with binary operation",
                      "6sad":"error : Not a Valid RPN, try until you succeed...e.g. 2 3 +",
                      "2 3 4 +":"error : Not a Valid RPN, try until you succeed...e.g. 2 3 +",
                      "-6":"error : Not a Valid RPN, try until you succeed...e.g. 2 3 +",
                      "!":"error : Not enough Operands to proceed with unary operation",
                      "%":"error : Not enough Operands to proceed with unary operation"
                  }
    for expression , expected_output in test_io_cases.iteritems():
        actual_op = RPN.evaluate_expression(expression)
        print "Output is %s for %s" % (expected_output,expression)
        assert   actual_op == expected_output
