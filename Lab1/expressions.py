from stack import StackArray
class Expressions():
    def __init__(self, string, type):
        self.string = string

        self.type = type
        self.valid_types = ['Prefix','Postfix','Infix']
        if self.type not in self.valid_types:
            print(f"The type you entered: {type}, is incorrect. Please enter a type from the following: {self.valid_types}")

    def to_post_fix(self):
        if self.type == 'Prefix':
            return self.pre_to_post()     
        elif self.type == 'Infix':
            print("Process does not exist at the moment! Try again another time.")
        else:
            pass
        
    def to_pre_fix(self):
        if self.type == 'Postfix':
            self.post_to_pre()
        elif self.type == 'Infix':
            print("Process does not exist at the moment. Try again another time.")

    def to_infix(self):
        if self.type =='Prefix':
           self.pre_to_infix()
        elif self.type == 'Postfix':
           self.post_to_infix()
        else:
            return self.string
               
    operators = ['+','-','/','*','$','(',')']

    def pre_to_post(self):
        stack = StackArray()
        for char in self.reverse_order(self.string):
            if char not in Expressions.operators: 
                stack.push(char)
            elif char in Expressions.operators:
                    pop1 = stack.pop()
                    pop2 = stack.pop()
                    push_items = [pop1,pop2,char]
                    push = ''.join([item for item in push_items if item != None])
                    stack.push(push) 
        if stack.stack_length() > 1:
            pos_string = ''
            while stack.empty()!= True:
                pos_string = pos_string + stack.pop()
            return pos_string
        else:
            return stack.return_object()[0]


    def post_to_pre(self):
        stack = StackArray()
        for char in self.string:
            if char not in Expressions.operators: 
                stack.push(char)
            elif char in Expressions.operators:
                pop1 = stack.pop()
                pop2 = stack.pop()
                stack.push(pop1+pop2+char)
        print(self.reverse_order(stack.return_object()[0]))

    def pre_to_infix(self):
        stack = StackArray()
        for char in self.reverse_order(self.string):
            if char not in Expressions.operators: 
                stack.push(char)
            elif char in Expressions.operators:
                pop1 = stack.pop()
                pop2 = stack.pop()
                stack.push(f"({pop1}{char}{pop2})")
        #stack.display_stack()
        print(stack.return_object()[0])

    def post_to_infix(self):
        stack = StackArray()
        for char in self.string:
            if char not in Expressions.operators: 
                stack.push(char)
            elif char in Expressions.operators:
                pop1 = stack.pop()
                pop2 = stack.pop()
                stack.push(f"({pop2}{char}{pop1})")
        #stack.display_stack()
        print(stack.return_object()[0])

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
        
