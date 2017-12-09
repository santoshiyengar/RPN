import re

# Class made for customized Math functions...
class RPNMath(object):
    
    # Get Percentage value.
    @staticmethod
    def percentage(a):
        return a/100;  
    
    # Check the Number's Validity.
    @staticmethod
    def is_valid_number(num):
        """ Returns True is string is a number. """
        if re.match("^\d+?\.\d+?$", num) is None:
            return num.isdigit()
        return True