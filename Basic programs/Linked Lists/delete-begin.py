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
            while self.head.next != None:
                print(self.head.data,'-->',end='')
                self.head = self.head.next
            print(self.head.data)    
    def insertBegin(self,data):
        newnode = Node(data)
        newnode.next = self.head
        self.head = newnode
        
    def insertEnd(self,data):
        newnode = Node(data)
        curr = self.head
        while curr.next != None:
            curr=curr.next
        curr.next = newnode
        
    def deleteBegin(self):
        self.head = self.head.next
l1=LinkedList()
l1.insertBegin(10)
l1.insertEnd(40)
l1.insertBegin(20)
l1.insertEnd(30)
l1.insertBegin(50)
l1.insertEnd(60)
l1.deleteBegin()
l1.traverse()

