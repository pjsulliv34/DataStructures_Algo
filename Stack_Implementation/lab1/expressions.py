from lab1.stack import StackArray
from lab1.operand import Operands
class Expressions():
    """
    The Expression class enables users to convert from Postfix to Prefix and Infix and Prefix to Postfix and Infix. We currently do 
    not have infix to postfix and prefix, but that can be a future enhancement. The Expression object takes in a Postfix, Prefix or Infix 
    as a string. Then we have three main methods, to postfix, to prefix and to infix. These methods, use the input type to verify the process 
    required in order to convert to the desired expression. Once the process has been confirmed, then the method calls on one of the four 
    methods to convert from the input type to the desired output type. The last method in the class is the reverse order method. This method 
    takes in a string and reverses the order of the string using the imported stack method.
    """

    # Initialize class instance variables
    def __init__(self, string, input_type):
        self.string = string
        self.input_type = input_type
        self.valid_types = ['Prefix','Postfix','Infix']
        # This is a method to notify the user if they entred an incorrect input type when creating the Expression Object
        if self.input_type not in self.valid_types:
            print(f"The type you entered: {input_type}, is incorrect. Please enter a type from the following: {self.valid_types}")


    # This Method uses the inputy type to select the correct method in order to convert from the input type to the desired output type.
    def to_post_fix(self):
        if self.input_type == 'Prefix':
            return self.pre_to_post()     
        elif self.input_type == 'Infix':
            return "Process does not exist at the moment! Try again another time."
        else:
            return self.string

    # This Method uses the inputy type to select the correct method in order to convert from the input type to the desired output type.    
    def to_pre_fix(self):
        if self.input_type == 'Postfix':
            return self.post_to_pre()
        elif self.input_type == 'Infix':
            return "Process does not exist at the moment. Try again another time."
        else:
            return self.string
        
    # This Method uses the inputy type to select the correct method in order to convert from the input type to the desired output type.
    def to_infix(self):
        if self.input_type =='Prefix':
           return self.pre_to_infix()
        elif self.input_type == 'Postfix':
           return self.post_to_infix()
        else:
            return self.string

    # Initialize a list of operators that is used in the methods below.         
    operators = ['+','-','/','*','$']

    # This Method converts from prefix to post fix
    def pre_to_post(self):

        # Initialize a Stack using the stack class
        stack = StackArray()
        # Loop through each character in the string in reverse order
        for char in self.reverse_order(self.string):

            # Check to see if string in the class variable operators
            if char not in Expressions.operators: 

                # Use stack method to push character into stack
                stack.push(char)

            # Check to see character in operators   
            elif char in Expressions.operators:
                    
                    # Use stack methods to pop top two elements off
                    pop1 = stack.pop()
                    pop2 = stack.pop()
                    
                    # Create an operand object using the operand class
                    operand = Operands(pop1,pop2,char,'Pre_Post')

                    # Check to see if any of the pops are none. If so return error, otherwise continue with pushing on stack
                    if operand.combine_operands() == 'None-Type':
                        return "Incorrect Number of Operands"
                    else:
                        stack.push(operand.combine_operands())    
        
        # Additional Check to see if the stack is longer than one element. If so, return error, otherwise pop full string out of stack.
        if stack.stack_length()>1:
            return 'Incorrect Number of Operators' 
        else:
            return stack.pop()
        

    # This Method Converts from Postfix to Prefix
    def post_to_pre(self):
        stack = StackArray()
        for char in self.string:
            if char not in Expressions.operators: 
                stack.push(char)
            elif char in Expressions.operators:
                pop1 = stack.pop()
                pop2 = stack.pop()
                operand = Operands(pop1,pop2,char,'Post_Pre')
                if operand.combine_operands() == 'None-Type':
                        return "Incorrect Number of Operands"
                else:
                    stack.push(operand.combine_operands())    
        if stack.stack_length()>1:
            return 'Incorrect Number of Operators' 
        else:
            # We need to reverse the order of the final stack item in order to have the prefix string 
            # in the correct order
            return self.reverse_order(stack.pop())


    # This methood converts from prefix to infix
    def pre_to_infix(self):
        stack = StackArray()
        for char in self.reverse_order(self.string):
            if char not in Expressions.operators: 
                stack.push(char)
            elif char in Expressions.operators:
                pop1 = stack.pop()
                pop2 = stack.pop()
                operand = Operands(pop1,pop2,char,'Pre_Infix')
                if operand.combine_operands() == 'None-Type':
                    return "Incorrect Number of Operands"
                else:
                    stack.push(operand.combine_operands())    
        if stack.stack_length()>1:
            return 'Incorrect Number of Operators' 
        else:
            return stack.pop()

    # This Method converts from postfix to infix
    def post_to_infix(self):
        stack = StackArray()
        for char in self.string:
            if char not in Expressions.operators: 
                stack.push(char)
            elif char in Expressions.operators:
                pop1 = stack.pop()
                pop2 = stack.pop()
                operand = Operands(pop1,pop2,char,'Post_Infix')
                if operand.combine_operands() == 'None-Type':
                    return "Incorrect Number of Operands"
                else:
                    stack.push(operand.combine_operands())    
        if stack.stack_length()>1:
            return 'Incorrect Number of Operators' 
        else:
            return stack.pop()

    # This Method takes a string and reverses the order
    def reverse_order(self,string):

        # Initialize a Stack
        stack = StackArray()
        
        # Loop through each character in string
        for char in string:
            # Push character onto stack
            stack.push(char)

        # Initialize an empty string
        reverse_string = ''
        
        # while loop to verify that the stack is not empty
        while stack.empty() == False:

            # set char variable to reference top of item on stack
            char = stack.pop()
            
            # Append string with characgter from stack
            reverse_string = reverse_string+char  

        # Return reversed string
        return reverse_string
        

    
   