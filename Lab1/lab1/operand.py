class Operands:
    def __init__(self,op1,op2,char,type):
        self.op1 = op1
        self.op2 = op2
        self.char = char
        self.type = type
        self.valid_types = ['Post_Pre', 'Pre_Post','Pre_Infix','Post_Infix']
        if self.type not in self.valid_types:
            print(f"The type you entered: {type}, is incorrect. Please enter a type from the following: {self.valid_types}")

    def combine_operands(self):
        if self.type in ['Post_Pre', 'Pre_Post']:
            return self.combine_post_and_prefix()
        elif self.type == 'Pre_Infix':
            return self.combine_pre_infix()
        else: 
            return self.combine_post_infix()

    def combine_post_and_prefix(self):
        if self.check_for_None() == False:
            opperand = self.op1 + self.op2 + self.char
            return opperand
        else:
            return "None-Type"
    

    def combine_pre_infix(self):
        if self.check_for_None() == False:
            operand = self.op1 + self.char + self.op2
            return operand
        else:
            return "None-Type"

    
    def combine_post_infix(self):
        if self.check_for_None() == False:
            operand = self.op2 + self.char + self.op1
            return operand
        else:
            return "None-Type"
        
        
    def check_for_None(self):
        if self.op1 is None or self.op2 is None or self.char is None:
            return True
        else: 
            return False


