from rpn import RPN
 
def main():
    
    # Display Help in the beginning of the program.
    print RPN.rpn_help()
    
    # Get into a controlled Daemon/infinite loop.
    while True:
        
        # Get the RPN expression
        input_text = RPN.get_input()
        
        # Check what have you got, if its an expression, call for evaluation
        if RPN.is_expression(input_text):
            output = RPN.evaluate_expression(input_text)
            print output
        
if __name__ == "__main__":
    main()
    