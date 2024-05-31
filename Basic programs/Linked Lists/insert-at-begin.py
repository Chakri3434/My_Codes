class Node:
    
    def __init__(self,data):
        self.data = data
        self.next = None
        
class LinkedList:
    
    def __init__(self):
        self.head = None
        
    def traverse(self):
        if self.head is None:
            print('The linked list is empty')
        else:
            while self.head != None:
                print(self.head.data)
                self.head = self.head.next
                
    def insertBegin(self,data):
        newnode = Node(data)
        newnode.next = self.head
        self.head = newnode
        
l1=LinkedList()
l1.insertBegin(10)
l1.insertBegin(20)
l1.traverse()
