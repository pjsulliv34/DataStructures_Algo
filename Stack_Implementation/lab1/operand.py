class Operands:
    """
    This class creates an Operand object using two operands, a operator, and the input type. The class has a main method called combine operands.
    This method using the type to verify which method to run to get the desired combined string. For example if Post_Pre is the type, then the combine
    operands method will call on the combine post and prefix method which combines the operand in the desired format and returns a string.
    """

    # Initialize class instance variables
    def __init__(self,op1,op2,operator,type):
        self.op1 = op1
        self.op2 = op2
        self.operator = operator
        self.type = type
    
    # This method uses the type to verify what method below to call and return
    def combine_operands(self):
        if self.type in ['Post_Pre', 'Pre_Post']:
            return self.combine_post_and_prefix()
        elif self.type == 'Pre_Infix':
            return self.combine_pre_infix()
        else: 
            return self.combine_post_infix()

    # This method works for an input type of post_pre and pre_post
    def combine_post_and_prefix(self):

        # If Clause to check if any of the opeartors and operands are None
        if self.check_for_None() == False:

            # Create desired combined string in correct format
            combined = self.op1 + self.op2 + self.operator
            return combined
        
        # Return None-type error if there are none type for any operators or operands.
        else:
            return "None-Type"
    
    # This method works for a input type of Pre_Infix
    def combine_pre_infix(self):
        if self.check_for_None() == False:

            # Creates a combined string expected of an infix expression
            combined = '('+ self.op1 + self.operator + self.op2+')'
            return combined
        else:
            return "None-Type"

    # This method is called if none of the other methods are called first.
    def combine_post_infix(self):
        if self.check_for_None() == False:

            # Creates a combined string as desired for a postfix to infix conversion
            operand = '('+self.op2 + self.operator + self.op1+')'
            return operand
        else:
            return "None-Type"
        
    # This is a helper method to check if any of the class instance variables are none
    def check_for_None(self):

        # If clause to check if class instance variables are none
        if self.op1 is None or self.op2 is None or self.operator is None:

            # Return True is so otherwise false
            return True
        else: 
            return False


