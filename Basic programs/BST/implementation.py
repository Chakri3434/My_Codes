class TreeNode:
    def __init__(self,value):
        self.val=value
        self.left=None
        self.right=None
    def insert(self,value):
        if value<self.val:
            if self.left:
                self.left.insert(value)
            else:
                self.left=TreeNode(value)
        else:
            if self.right:
                self.right.insert(value)
            else:
                self.right=TreeNode(value)
    def inorder(self):
        if self.left:self.left.inorder()
        print(self.val)
        if self.right:self.right.inorder()
tree=TreeNode(50)
tree.insert(30)
tree.insert(10)
tree.insert(40)
tree.insert(70)
tree.insert(60)
tree.insert(80)
tree.inorder()
