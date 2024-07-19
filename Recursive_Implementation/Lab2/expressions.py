from Lab2.stack import StackArray
from Lab2.operand import Operands
class Expressions:
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
    def pre_to_post(self, postfix = None, index = 0):
        if postfix == None:
            postfix = []
        if index >= len(self.string):
            print(f'final postfix {postfix}')
            if len(postfix) >1:
                return 'Incorrect Number of Operators'
            else:
                final_item = postfix.pop()
                return final_item
        char = self.reverse_order(self.string)[index]
        if char not in Expressions.operators:
            postfix.append(char)
            index +=1
            return self.pre_to_post(postfix, index)
        else:
            if len(postfix) <2:
                return "Incorrect Number of Operands"
            else:
                item1 = postfix.pop()
                item2 = postfix.pop()
                operand = Operands(item1,item2,char,'Pre_Post')
                postfix.append(operand.combine_operands())
                index +=1
                return self.pre_to_post(postfix, index)

     

    # This Method Converts from Postfix to Prefix
    def post_to_pre(self, prefix = None, index = 0):
        if prefix == None:
            prefix = []
        if index >= len(self.string):
            if len(prefix) >1:
                return 'Incorrect Number of Operators'
            else:
                final_item = prefix.pop()
                return self.reverse_order(final_item)
        char = self.string[index]
        if char not in Expressions.operators:
            prefix.append(char)
            index +=1
            return self.post_to_pre(prefix, index)
        else:
            if len(prefix) <2:
                return "Incorrect Number of Operands"
            else:
                item1 = prefix.pop()
                item2 = prefix.pop()
                operand = Operands(item1,item2,char,'Post_Pre')
                prefix.append(operand.combine_operands())
                index +=1
                return self.post_to_pre(prefix, index)


    # This methood converts from prefix to infix
    def pre_to_infix(self, infix = None, index = 0):
        if infix == None:
            infix = []
        if index >= len(self.string):
            print(f'final postfix {infix}')
            if len(infix) >1:
                return 'Incorrect Number of Operators'
            else:
                final_item = infix.pop()
                return final_item
        char = self.reverse_order(self.string)[index]
        if char not in Expressions.operators:
            infix.append(char)
            index +=1
            return self.pre_to_infix(infix, index)
        else:
            if len(infix) <2:
                return "Incorrect Number of Operands"
            else:
                item1 = infix.pop()
                item2 = infix.pop()
                operand = Operands(item1,item2,char,'Pre_Infix')
                infix.append(operand.combine_operands())
                index +=1
                return self.pre_to_infix(infix, index)
        

    # This Method converts from postfix to infix
    def post_to_infix(self, infix = None, index = 0):
        if infix == None:
            infix = []
        if index >= len(self.string):
            print(f'final postfix {infix}')
            if len(infix) >1:
                return 'Incorrect Number of Operators'
            else:
                final_item = infix.pop()
                return final_item
        char = self.string[index]
        if char not in Expressions.operators:
            infix.append(char)
            index +=1
            return self.post_to_infix(infix, index)
        else:
            if len(infix) <2:
                return "Incorrect Number of Operands"
            else:
                item1 = infix.pop()
                item2 = infix.pop()
                operand = Operands(item1,item2,char,'Post_Infix')
                infix.append(operand.combine_operands())
                index +=1
                return self.post_to_infix(infix, index)
        
    def reverse_order(self, string):
        if len(string) == 0:
            return string   
        return string[-1] + self.reverse_order(string[:-1])

    # # This Method takes a string and reverses the order
    # def reverse_order(self,string):

    #     # Initialize a Stack
    #     stack = StackArray()
        
    #     # Loop through each character in string
    #     for char in string:
    #         # Push character onto stack
    #         stack.push(char)

    #     # Initialize an empty string
    #     reverse_string = ''
        
    #     # while loop to verify that the stack is not empty
    #     while stack.empty() == False:

    #         # set char variable to reference top of item on stack
    #         char = stack.pop()
            
    #         # Append string with characgter from stack
    #         reverse_string = reverse_string+char  

    #     # Return reversed string
    #     return reverse_string

       

    
        

    
   