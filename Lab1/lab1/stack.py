class StackArray: 
    def __init__(self): 
        self.stack = []
 
    def empty(self):
        if len(self.stack) ==0 :
            return True
        else:
            return False
    
    def peek(self):
        if self.empty() == False:
            return self.stack[len(self.stack)-1]
        else:
            print('Stack is Empty')

    def pop(self):
        if self.empty() == False:
            item = self.stack[-1]
            self.stack = self.stack[:-1]
            return item

    def stack_length(self):
        return len(self.stack)

    def push(self,item):
        self.stack.append(item)

    def display_stack(self):
        print(self.stack)

    def return_object(self):
        return self.stack