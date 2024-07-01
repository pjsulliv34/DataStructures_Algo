from lab1.stack import StackArray
from lab1.operand import Operands
class Expressions():
    def __init__(self, string, input_type):
        self.string = string
        self.input_type = input_type
        self.valid_types = ['Prefix','Postfix','Infix']
        if self.input_type not in self.valid_types:
            print(f"The type you entered: {input_type}, is incorrect. Please enter a type from the following: {self.valid_types}")

    def to_post_fix(self):
        if self.input_type == 'Prefix':
            return self.pre_to_post()     
        elif self.input_type == 'Infix':
            return "Process does not exist at the moment! Try again another time."
        else:
            return self.string
        
    def to_pre_fix(self):
        if self.input_type == 'Postfix':
            return self.post_to_pre()
        elif self.input_type == 'Infix':
            return "Process does not exist at the moment. Try again another time."
        else:
            return self.string

    def to_infix(self):
        if self.input_type =='Prefix':
           return self.pre_to_infix()
        elif self.input_type == 'Postfix':
           return self.post_to_infix()
        else:
            return self.string
               
    operators = ['+','-','/','*','$','(',')']

    def pre_to_post(self):
        stack = StackArray()
       # print(f'Start: {self.string}')
        for char in self.reverse_order(self.string):
            if char not in Expressions.operators: 
                stack.push(char)
            elif char in Expressions.operators:
                    pop1 = stack.pop()
                    pop2 = stack.pop()
                    #print(f'{pop1},{pop2}{char}')
                    operand = Operands(pop1,pop2,char,'Pre_Post')
                    if operand.combine_operands() == 'None-Type':
                        return "Incorrect Number of Operands"
                    else:
                        stack.push(operand.combine_operands())    
        
        if stack.stack_length()>1:
            return 'Incorrect Number of Operators' 
        else:
            return stack.pop()
        


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
            return self.reverse_order(stack.pop())


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
        stack.display_stack()
        if stack.stack_length()>1:
            return 'Incorrect Number of Operators' 
        else:
            return stack.pop()

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
        stack.display_stack()
        if stack.stack_length()>1:
            return 'Incorrect Number of Operators' 
        else:
            return stack.pop()

    def reverse_order(self,string):
        stack = StackArray()
        for char in string:
            #print(char)
            stack.push(char)
        reverse_string = ''
        #stack.display_list()
        while stack.empty() == False:
            char = stack.pop()
            #print(char)
            reverse_string = reverse_string+char  
        return reverse_string
        

    
   