
from Lab2.operand import Operands
class Expressions:
    """
    The Expression class enables users to convert from Postfix to Prefix and Infix and Prefix to Postfix and Infix. We currently do 
    not have infix to postfix and prefix, but that can be a future enhancement. The Expression object takes in a Postfix, Prefix or Infix 
    as a string. Then we have three main methods, to postfix, to prefix and to infix. These methods, use the input type to verify the process 
    required in order to convert to the desired expression. Once the process has been confirmed, then the method calls on one of the four 
    methods to convert from the input type to the desired output type. The last method in the class is the reverse order method. This method 
    takes in a string and reverses the order of the string recursively processing each item in the string.
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

        # Check to see if a postfix list has been inputed into the function
        if postfix == None:

            # Initialize Empty list
            postfix = []

        # Base Case of recursive function. 
        if index >= len(self.string):

            # If clause to check if length of postfix list is greater than 1, if so, return error, else return final element in list
            if len(postfix) >1:
                return 'Incorrect Number of Operators'
            else:
                final_item = postfix.pop()
                return final_item
            
        # Grab current element in recursive call based on inputed index
        # List is reverse before traversing to grab element    
        char = self.reverse_order(self.string)[index]

        # Check to see if char in the class variable operators
        if char not in Expressions.operators:

            # If not add char to postfix list and increment index
            postfix.append(char)
            index +=1

            # Recursive call to pre_to_post function
            return self.pre_to_post(postfix, index)
        
        # Else clause assumes character not in class variable operators
        else:

            # Check to see if the postfix list is less than 2 elements, if so, return error
            if len(postfix) <2:
                return "Incorrect Number of Operands"
            else:

                # Use pop function to grab the first two elements in postfix list
                item1 = postfix.pop()
                item2 = postfix.pop()

                # Create an operand object using the operand class
                operand = Operands(item1,item2,char,'Pre_Post')

                # Using operand method, append list with new opperand. Increment index by 1.
                postfix.append(operand.combine_operands())
                index +=1

                # Recursive call to pre_to_post function
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

                # reverse the string before returning the final prefix string.
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
            
    # This Method takes a string and reverses the order of the string.    
    def reverse_order(self, string):

        # If clause to check if the string length equals 0
        if len(string) == 0:
            return string  

        # Recursive call grabbing last element and string to the last element inclusive 
        return string[-1] + self.reverse_order(string[:-1])


       

    
        

    
   