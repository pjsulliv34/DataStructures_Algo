class StackArray: 
    """
    This class is used to simulate a stack object using pythons built in list data structure. We have 5 methods that are included. Empty tells us if
    the stack is empty. Peek allows us to look at the item at the top of the stack with out modifying it. Pop allows us to grab the last item of the
    stack and modify it. Stack length tells us the length of the current stack. Push pushes the item to the top of the stack.
    """

    # Initialize class instance variable
    def __init__(self): 

        # Initialize an empty list called stack
        self.stack = []
 
    # Method to determine if stack is empty
    def empty(self):

        # If length of stack is 0 return True otherwise return false
        if len(self.stack) ==0 :
            return True
        else:
            return False
    
    # Method to return value at top of stack
    def peek(self):

        # First check to see if stack is empty before returning value in stack
        if self.empty() == False:

            # Return value at top of stack using the last index of list
            return self.stack[len(self.stack)-1]
        else:
            # Prints message if its impossible to peek an item that does not exist!
            print('Stack is Empty')

    # Method to return the item at top of stack and remove that item from stack
    def pop(self):

        # Checks to see if the stack is empty
        if self.empty() == False:

            # Sets item at top of stack to reference item variable using last index
            item = self.stack[-1]

            # Removes the item from stack using indices
            self.stack = self.stack[:-1]

            # Returns the item at top of stack
            return item

    # Method to return the length of the stack
    def stack_length(self):

        # Returns the length of stack using the len function
        return len(self.stack)

    # Method to push item to top of stack
    def push(self,item):

        # Does not return anything, just pushes item to top of stack using the list append function
        self.stack.append(item)



