# Create Priority Queue
class TreeSearch:
    def __init__(self, value, char, left = None, right = None ):
        self.value = value
        self.left = left
        self.right = right
        self.char = char

    def insert(self, value, char):
        if value < self.value:
            if self.left is None:
                self.left = TreeSearch(value, char)
            else:
                self.left.insert(value, char)
        else:
            if self.right is None:
                self.right = TreeSearch(value, char)
            else:
                self.right.insert(value, char)

    def sort_tree(self, sorted_list = []):
        if self.left:
            self.left.sort_tree()
        sorted_list.append([self.value, self.char])
        if self.right:
            self.right.sort_tree()
        return sorted_list
    
    def reverse_order(self,list_):

        # Base Case of recursive function
        if len(list_) == 0:
            return list_  

        # Recursive call grabbing last element and string to the last element inclusive 
        return [list_[-1]] + self.reverse_order(list_[:-1])
    

    def build_Huffman_tree(self, sorted_nodes):
        alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

        while len(sorted_nodes) >1:
            pop1 = sorted_nodes.pop()
            pop2 = sorted_nodes.pop()

            if pop1.value == pop2.value:
                if len(pop1.char) == 1 and len(pop2.char)>1:
                    left = pop1
                    right = pop2
                if len(pop2.char) == 1 and len(pop1.char)>1:
                    left = pop2
                    right = pop1
                if len(pop1.char) == 1 and len(pop2.char)==1:
                    pop1_pos = 0
                    pop2_pos = 0
                    while pop1 != alpha[pop1_pos]:
                        pop1_pos+=1
                    while pop2 != alpha[pop2_pos]:
                        pop2_pos+=1
                    if pop1_pos< pop2_pos:
                        left = pop1
                        right = pop2
                    else:
                        left = pop2
                        right = pop1   

            else:
                right = pop1
                left = pop2  
            val = left.value + right.value
            char = left.char + right.char
            parent_node = TreeSearch(val,char, left, right )  
            sorted_nodes.append(parent_node)
         
       # print(sorted_nodes[0].char)
       # print(sorted_nodes[0].value)
        return sorted_nodes[0]

    def preOrderTraversal(self,node):
        if node is None:
            return

        # Deal with the node
        print(f'{node.value} : {node.char}')

        # Recur on left subtree
        self.preOrderTraversal(node.left)

        # Recur on right subtree
        self.preOrderTraversal(node.right)

    
    def get_huffman_codes(self,huffman_tree, huffman_list = [], prefix = ''):
        if huffman_tree.left is None and huffman_tree.right is None:
            huffman_list.append([huffman_tree.char,prefix])
        else:
            if huffman_tree.left is not None:
                self.get_huffman_codes(huffman_tree.left,  huffman_list , prefix +'0')
            if huffman_tree.right is not None:
                self.get_huffman_codes(huffman_tree.right,  huffman_list , prefix +'1')
        return  huffman_list
   


    
index = 0
for value in freq_table:
        if index == 0:
                tree = TreeSearch(value[1],value[0])
                index +=1
        else:
                tree.insert(value[1],value[0])
sorted = tree.sort_tree()
print(sorted)



reverse_sorted = tree.reverse_order(sorted)
print(reverse_sorted)


# tree.build_Huffman_tree(reverse_sorted)
node_list = [TreeSearch(val[0],val[1]) for val in reverse_sorted]
print(node_list)
for val in node_list:
        print(val.value)
huffman = tree.build_Huffman_tree(node_list)
print(huffman)
#print(huffman.left.left.value)
tree.preOrderTraversal(huffman)
huffman_code = tree.get_huffman_codes(huffman)
print(huffman_code)









