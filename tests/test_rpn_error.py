from rpn_error import ErrorHandler 
import rpn_error

# Check Message for Invalid RPN....
def test_get_error_message():
    assert ErrorHandler.get_error_message('ERROR_INVALID_RPN') == 'error : Not a Valid RPN, try until you succeed...e.g. 2 3 +'

# Check Message for invalid Binary Operations.
def test_get_error_message_binary_operation():
    assert ErrorHandler.get_error_message('ERROR_INVALID_BINARY_OPERATION') == 'error : Not enough Operands to proceed with binary operation'

# Check Message for invalid Unary Operations
def test_get_error_message_unary_operation():
    assert ErrorHandler.get_error_message('ERROR_INVALID_UNARY_OPERATION') == 'error : Not enough Operands to proceed with unary operation'

# Check Exixtence of error Dictionary
def test_existence_error_dictionary(): 
    assert isinstance(rpn_error.ERRORS, dict)
    assert rpn_error.ERRORS == {
          "ERROR_INVALID_RPN":'error : Not a Valid RPN, try until you succeed...e.g. 2 3 +' ,
          "ERROR_INVALID_BINARY_OPERATION":'error : Not enough Operands to proceed with binary operation',
          "ERROR_INVALID_UNARY_OPERATION": 'error : Not enough Operands to proceed with unary operation'        
        } 