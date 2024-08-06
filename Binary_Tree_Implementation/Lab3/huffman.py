# Create Priority Queue
from Lab3.tree_node import TreeSearch

class Huffman:

    def build_Huffman_tree(self, sorted_nodes):
        while len(sorted_nodes) >1:
            left = sorted_nodes.pop()
            right = sorted_nodes.pop()
            val = left.value + right.value
            char = left.char + right.char
            parent_node = TreeSearch(val, char, left, right )  
            sorted_nodes.append(parent_node)
            sorted_nodes = self.sort_priority(sorted_nodes)      
        return sorted_nodes[0]
  
    def get_huffman_codes(self,huffman_tree, huffman_list = [], prefix = ''):
        if huffman_tree.left is None and huffman_tree.right is None:
            huffman_list.append([huffman_tree.char,prefix])
        else:
            #print(f'{huffman_tree.left.value} left, {huffman_tree.right.value} right')
            if huffman_tree.left is not None:
                self.get_huffman_codes(huffman_tree.left,  huffman_list , prefix +'0')
            if huffman_tree.right is not None:
                self.get_huffman_codes(huffman_tree.right,  huffman_list , prefix +'1')
        return  huffman_list
    
    def sort_priority(self,list_):
        stack = []
        alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        while list_:
            current = list_.pop()
            # Insert current element into the correct position in the stack
            temp_stack = []
            current_index = 0
            current_stack_index = 0
            for i in alpha:
                if current.char == alpha[current_index]:
                    break
                else:
                    current_index +=1
            for i in alpha:
                if stack and stack[-1].char == alpha[current_stack_index]:
                    break
                else:
                    current_stack_index+=1
            while stack and (stack[-1].value < current.value or 
                            (stack[-1].value == current.value and len(stack[-1].char) < len(current.char)) or
                            (stack[-1].value == current.value and len(stack[-1].char) == len(current.char) and current_stack_index < current_index)):
                temp_stack.append(stack.pop())
            
            stack.append(current)
            
            # Push back elements from the temporary stack to the main stack
            while temp_stack:
                stack.append(temp_stack.pop())
        
        return stack
        
    
    def encode_huffman( self, string, huffman_code):
        final = ''
        
        
        for c in string:
            
            for code in huffman_code:
                
                if c.lower() == code[0].lower():
                    final += code[1]
                    break  
       
        return final
    
    def decode_huffman(self,binary_string, huffman_code):
        final = ''
        temp_char = ''
        for c in binary_string:
            temp_char += c
            for code in huffman_code:
                if temp_char == code[1]:
                    final += code[0]
                    temp_char = ''
                    break  
        return final
    
    def preOrderTraversal(self,node, output = None):
        if output is None:
            output = []
        if node is None:
            return output
        

        # Deal with the node
        print(f'{node.value} : {node.char}')
        output.append([node.value,node.char])

        # Recur on left subtree
        self.preOrderTraversal(node.left, output)

        # Recur on right subtree
        self.preOrderTraversal(node.right, output)

        return output

        
        
    
   

   


    



