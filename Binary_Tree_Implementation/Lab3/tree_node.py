# Create Priority Queue
class TreeSearch:
    def __init__(self, value, char, left = None, right = None ):
        self.value = value
        self.left = left
        self.right = right
        self.char = char

    # def insert(self, value, char):
    #     if value < self.value:
    #         if self.left is None:
    #             self.left = TreeSearch(value, char)
    #         else:
    #             self.left.insert(value, char)
    #     else:
    #         if self.right is None:
    #             self.right = TreeSearch(value, char)
    #         else:
    #             self.right.insert(value, char)

    def sort_tree(self, sorted_list = []):
    
        if self.left:
            self.left.sort_tree()
        sorted_list.append(TreeSearch(self.value, self.char))
        #sorted_list.append([self.value, self.char])
        if self.right:
            self.right.sort_tree()
        
        return sorted_list
     

    def preOrderTraversal(self,node, output = []):

        if node is None:
            return

        # Deal with the node
        print(f'{node.value} : {node.char}')
        output.append([node.value,node.char])

        # Recur on left subtree
        self.preOrderTraversal(node.left)

        # Recur on right subtree
        self.preOrderTraversal(node.right)

    # def delete_tree(self):
    #     self.root = None  # This removes the reference to the root node

    # def delete_tree_nodes(self, node):
    #     if node:
    #         self.delete_tree_nodes(node.left)
    #         self.delete_tree_nodes(node.right)
    #         node.left = None
    #         node.right = None
    #         node.value = None

  
    
    