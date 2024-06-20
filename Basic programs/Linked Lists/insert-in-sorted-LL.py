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
    
    def deleteEnd(self):
        curr = self.head
        while curr.next.next != None:
            curr = curr.next
        curr.next = None
    
    def insertNode(self,data,position):
        newnode = Node(data)
        curr = self.head
        c = 1
        if position != 1:
            while c != position-1:
                curr = curr.next
                c+=1
            newnode.next = curr.next
            curr.next = newnode
        else:
            newnode.next = curr
            self.head = newnode
            
    def insertSorted(self,data):
        if self.head is None:
            return -1 
        curr = self.head
        position = 1
        while curr and data > curr.data:
            curr = curr.next
            position+=1
        return self.insertNode(data,position)
            
l1=LinkedList()
l1.insertBegin(60)
l1.insertBegin(50)
l1.insertBegin(40)
l1.insertBegin(30)
l1.insertBegin(20)
l1.insertBegin(10)
l1.insertSorted(65)
l1.traverse()
        
