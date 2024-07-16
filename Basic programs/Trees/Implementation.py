class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
        
class BinaryTree:
    def __init__(self,root):
        self.root = Node(root)
        
#          1 
#        /   \
#       2      3
#      / \    /  \
#     4   5  6    7
#                  \
#                   8

tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
tree.root.right.right.right = Node(8)
print(tree.root.left.left.val)
