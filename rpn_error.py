# Dictionary for error handling...
ERRORS = {
          "ERROR_INVALID_RPN":'error : Not a Valid RPN, try until you succeed...e.g. 2 3 +' ,
          "ERROR_INVALID_BINARY_OPERATION":'error : Not enough Operands to proceed with binary operation',
          "ERROR_INVALID_UNARY_OPERATION": 'error : Not enough Operands to proceed with unary operation'        
        }

# Class for Error handling.
class ErrorHandler(object):
        
        @classmethod
        def get_error_message(cls, error_msg):
            return ERRORS[error_msg];            