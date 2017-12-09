import operator
import math
from rpn_math import RPNMath
from rpn_error import ErrorHandler   

class RPN(object):
    # Binary Operators, ensure adding test case before you add an operator here. 
    binary_operators = {'+' : operator.add, 
                        '-' : operator.sub, 
                        '*' : operator.mul, 
                        '/' : operator.div,
                        '^' : operator.pow,
                        }
    
    # Unary Operators, ensure adding test case before you add an operator here.
    unary_operators = {
                       '!' : math.factorial,
                       '%' : RPNMath.percentage
                       } 
    
    # Getting the input from the Keyboard using the famous triple greater than ">>>"
    @classmethod
    def get_input(cls):
        return raw_input('>>> ') 

    # Displays the possible help from the help.txt
    @classmethod
    def rpn_help(cls):
        return  open("help.txt").read()
    
    # Checks for few valid operations and if not found, call it an expression
    @classmethod
    def is_expression(cls, input_text = None):
        
        if input_text == '': 
            print ErrorHandler.get_error_message('ERROR_INVALID_RPN')
            return False
        
        # Check if asking for help, and Provide help 
        elif input_text in ['h','help',]:
            print cls.rpn_help()
        
        # Check if wanting to quit, exit.
        elif input_text in ['q','quit']:
            exit()
        
        #if above two cases aren't true, assume its an Expression.    
        else:
            return True

    @classmethod
    def evaluate_expression(cls, expression = None):
        
        tokens = expression.split()     # Split the expression by space.
        stack = []                      # Reset the Stack for every iteration.   
        token_index = 0                 #Reset the Token Index for every Iteration.
               
        for token in tokens:
            token_index = token_index + 1
            # Check the validity of the Numbers 
            if RPNMath.is_valid_number(token):
                stack.append(float(token))
            
            #If Not numbers, check if they are Binary Operators
            elif token in RPN.binary_operators:
                if len(stack) < 2:
                    return ErrorHandler.get_error_message('ERROR_INVALID_BINARY_OPERATION')
                a = stack.pop()
                b = stack.pop()
                operation = RPN.binary_operators[token]
                stack.append(operation(b,a))

            #If Not numbers, check if they are Unary Operators
            elif token in RPN.unary_operators:
                if len(stack) < 1:
                    return ErrorHandler.get_error_message('ERROR_INVALID_UNARY_OPERATION')
                a = stack.pop()
                operation = RPN.unary_operators[token]
                stack.append(operation(a))

            # Its an error if none of the above match, Handle the error
            else:
                return ErrorHandler.get_error_message('ERROR_INVALID_RPN')
                cls.rpn_help()
                
        if token_index == len(tokens) and len(stack) > 1:
            return ErrorHandler.get_error_message('ERROR_INVALID_RPN')
        else:
            return int(stack[0])

