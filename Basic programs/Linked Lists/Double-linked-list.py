class Node:
    
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None
        
class DoubleLinkedList:
    
    def __init__(self):
        self.head = None
        
    def printLL(self):
        curr = self.head
        while curr != None:
            print(curr.data)
            curr = curr.next
    
    def insertBegin(self,data):
        newnode = Node(data)
        if self.head is None:
            newnode.prev = None
            self.head = newnode
        else:
            self.head.prev = newnode
            newnode.next = self.head
            self.head = newnode
            newnode.prev = None
        
    def insertEnd(self,data):
        newnode = Node(data)
        if self.head is None:
            newnode.prev = None
            self.head = newnode
        else:
            curr = self.head
            while curr.next != None:
                curr = curr.next
            curr.next = newnode
            newnode.prev = curr
            newnode.next = None

    def reverse(self):
        temp = None
        curr = self.head
        while curr!=None:
            temp = curr.prev
            curr.prev = curr.next
            curr.next = temp
            curr = curr.next
        if temp != None:
            self.head = temp.prev
            
dl1=DoubleLinkedList()
dl1.insertBegin(30)
dl1.insertBegin(40)
dl1.insertEnd(50)
dl1.insertBegin(20)
dl1.insertEnd(10)
dl1.reverse()
dl1.printLL()
        
