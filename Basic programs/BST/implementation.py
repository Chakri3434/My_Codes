class Tree:
    def __init__(self,val=None):
        self.value = val
        if self.value:
            self.left = Tree()
            self.right = Tree()
        else:
            self.left = None
            self.right = None
    def isempty(self):
        return (self.value == None)
    def insert(self,data):
        if self.isempty():
            self.value = data
            self.left = Tree()
            self.right = Tree()
        elif data < self.value:
            self.left.insert(data)
            return
        elif data > self.value:
            self.right.insert(data)
        elif data == self.value:
            return
    def inorder(self):
        if self.isempty():
            return []
        else:
            return self.left.inorder() + [self.value] + self.right.inorder()
    def search(self,data):
        if self.isempty():
            print('Not Found')
            return
        if data==self.value:
            print('Found')
            return
        if data<self.value:
            self.left.search(data)
        else:
            self.right.search(data)
tree=Tree(50)
tree.insert(30)
tree.insert(10)
tree.insert(40)
tree.insert(70)
tree.insert(60)
tree.insert(80)
print(tree.inorder())
tree.search(90)
