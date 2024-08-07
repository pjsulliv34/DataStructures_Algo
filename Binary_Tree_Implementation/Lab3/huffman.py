class Huffman:
    """
    This class is used as a TreeNode class with additional functionality. First, we initialize a tree node. This node has the additional 
    ability to specify an additional value called char which is useful in Huffman encoding. The Rest of the methods are useful in Huffman
    encoding. The Build Huffman tree takes in a list of sorted tree nodes and builds a huffman tree based on a specific priority queue.
    The get huffman codes reads in that huffman tree and creates a list that specifiys the path for each leaf to Root in a binary format.
    The encode and decode functions read in a string, either binary or characters and converts that string using the huffman code. 
    The sort priority utilizes a two stack like objects to sort the tree node lists based on value and character length/alphabetically for 
    certain situations. The final method, Pre Order Traversal allows the user to print out the tree in PreOrder.
    """
    # Initialize class instance variables
    def __init__(self, value, char = None, left = None, right = None ):
        self.value = value
        self.left = left
        self.right = right
        self.char = char

    # Build Huffman Tree
    def build_Huffman_tree(self, sorted_nodes):

        # Loop through sorted nodes list, checking length
        while len(sorted_nodes) >1:

            # Pop first two items in the list based on Priority Queue
            left = sorted_nodes.pop()
            right = sorted_nodes.pop()

            #Combine each value and characters
            val = left.value + right.value
            char = left.char + right.char

            # Create New parent node with corresponding children and new val/char
            parent_node = Huffman(val, char, left, right )  

            # Append Node to Sorted Nodes List
            sorted_nodes.append(parent_node)

            # Sort Priority Queue for next iteration
            sorted_nodes = self.sort_priority(sorted_nodes)   

        # Return Only TreeNode in the list   
        return sorted_nodes[0]
  
    # Recursive method to Assign binary strings to huffman tree paths
    def get_huffman_codes(self,huffman_tree, huffman_list = [], prefix = ''):

        # Check if we have reached the leaf, if so grab the prefix path and append to list
        if huffman_tree.left is None and huffman_tree.right is None:
            huffman_list.append([huffman_tree.char,prefix])
        else:
            # Methods to recursively run through node-child paths, recursively pass in prefix/huffman list
            # Left children get O's and right children get 1's
            if huffman_tree.left is not None:
                self.get_huffman_codes(huffman_tree.left,  huffman_list , prefix +'0')
            if huffman_tree.right is not None:
                self.get_huffman_codes(huffman_tree.right,  huffman_list , prefix +'1')
        return  huffman_list
    
    # Method to set up the Huffman priority Queue
    # Sorts a list of tree nodes
    def sort_priority(self,list_):
        # Initialize an empty list
        stack = []
        alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
                 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        # While tree node list is not empty
        while list_:

            # Pop the item at end of list
            current = list_.pop()

            # initalize empty temp list and indexs to be used for identify alphabetical index
            temp_stack = []
            current_index = 0
            current_stack_index = 0

            # For loops to check popped items location in alphabet
            for i in alpha:
                if current.char.upper() == alpha[current_index]:
                    break
                else:
                    current_index +=1

            # For loop to check top of stack items location in alphabet
            for i in alpha:

                # If the stack is not empty then grab alphabet location
                if stack and stack[-1].char.upper() == alpha[current_stack_index]:
                    break
                else:
                    current_stack_index+=1

            # Main function for sorting. Value is the main sorting, if the values are the same, we then sort based on length of char.
            # If char length the same, then we sort by alpha location
            while stack and (stack[-1].value < current.value or 
                            (stack[-1].value == current.value and len(stack[-1].char) < len(current.char)) or
                            (stack[-1].value == current.value and len(stack[-1].char) == len(current.char) and current_stack_index < current_index)):
                temp_stack.append(stack.pop())
            
            stack.append(current)
            
            # Push back priority items onto top of main stack
            while temp_stack:
                stack.append(temp_stack.pop())
        
        return stack
        
    # Encode a string of characters using huffman code
    def encode_huffman( self, string, huffman_code):

        # Initialize empty string
        final = ''
        
        # Loop through each character in string
        for c in string:
            
            # If character in huffman code, add that vvalue to the final encoded string
            for code in huffman_code:
                if c.lower() == code[0].lower():
                    final += code[1]
                    break  
        return final
    
    # Decode binary string using huffman code
    def decode_huffman(self,binary_string, huffman_code):

        # Initialize empty strings
        final = ''
        temp_char = ''
        
        # For each character in binary string if match in huffman code, pull character.
        # If no match add binary string to temp and keep checking huffman code until a match.
        # loop through entire binary string, adding matches to return string
        for c in binary_string:
            temp_char += c
            for code in huffman_code:
                if temp_char == code[1]:
                    final += code[0]
                    temp_char = ''
                    break  
        return final
    

    # Method to loop through the Tree object using PreOrder Traversal
    def preOrderTraversal(self,node, output = None):

        # Checks to see if output is none, and intializes empty list
        if output is None:
            output = []

        # Base case to end recursive call
        if node is None:
            return output
       
        # append output list with node value and characters
        output.append([node.value,node.char])

        # Recursive call on left node, passing in output list
        self.preOrderTraversal(node.left, output)

        # Recursive call on right node, passing in output list
        self.preOrderTraversal(node.right, output)

        return output
    
    # Method to loop through the Tree object using PreOrder Traversal
    def post_OrderTraversal(self,node, output = None):

        # Checks to see if output is none, and intializes empty list
        if output is None:
            output = []

        # Base case to end recursive call
        if node is None:
            return output

        # Recursive call on left node, passing in output list
        self.post_OrderTraversal(node.left, output)

        # Recursive call on right node, passing in output list
        self.post_OrderTraversal(node.right, output)

        # append output list with node value and characters
        output.append([node.value,node.char])

        return output
    
    # Method to loop through the Tree object using PreOrder Traversal
    def in_OrderTraversal(self,node, output = None):

        # Checks to see if output is none, and intializes empty list
        if output is None:
            output = []

        # Base case to end recursive call
        if node is None:
            return output

        # Recursive call on left node, passing in output list
        self.in_OrderTraversal(node.left, output)

        # append output list with node value and characters
        output.append([node.value,node.char])

        # Recursive call on right node, passing in output list
        self.in_OrderTraversal(node.right, output)

        return output

        
        
    
   

   


    



