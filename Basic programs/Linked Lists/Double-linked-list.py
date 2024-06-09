class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
class DLinkedList:
    def __init__(self):
        self.head = None
    
    def print(self):
        if self.head is None:
            print('Linked list is empty')
        else:
            while self.head!=None:
                print(self.head.data)
                self.head = self.head.next
    
    def addatBegin(self,data):
        newnode = Node(data)
        if self.head is None:
            newnode.prev =None
            self.head = newnode
        else:
            self.head.prev = newnode
            newnode.next = self.head
            newnode.prev = None
            self.head = newnode
            
    def addatEnd (self,data):
        newnode = Node(data)
        if self.head is None:
            newnode.prev =None
            self.head = newnode
        else:
            curr=self.head
            while curr.next!=None:
                curr=curr.next
            curr.next=newnode
            newnode.prev = curr
            newnode.next = None
    
    def reverse(self):
        curr=self.head
        temp = None
        while curr!=None:
            temp = curr.prev
            curr.prev = curr.next
            curr.next = temp
            curr = curr.prev
        if temp:
            self.head = temp.prev
            
    def deleteBegin(self):
        curr = self.head
        curr = curr.next
        if curr==None:
            self.head = None
        else:
            curr.prev = None
            self.head = curr
l1=DLinkedList()
l1.addatBegin(20)
l1.addatBegin(30)
l1.addatEnd(40)
l1.addatBegin(50)
l1.addatEnd(70)
l1.reverse()
l1.deleteBegin()

l1.print()
            
