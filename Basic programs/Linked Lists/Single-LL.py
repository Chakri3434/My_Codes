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
                print(self.head.data,'--> ',end='')
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
            
    def middleofLL(self):
        if self.head is None:
            return -1
        slow=self.head
        fast=self.head
        while fast!=None and fast.next!=None:
            slow = slow.next
            fast = fast.next.next
        print(slow.data)
    """
    NAIVE METHOD
    
    def NthNodefromEnd(self,n):
        curr = self.head
        length=1
        while curr.next != None:
            length+=1
            curr = curr.next
        curr = self.head
        if length < n :
            return 
        for i in range(length-n):
            curr = curr.next
        print(curr.data)
    """
    def NthNodefromEnd(self,n):
        if self.head is None:
            return -1
        left = self.head
        right = self.head
        for i in range(n):
            right = right.next
        while right != None:
            right = right.next
            left = left.next
        print(left.data)
        
    def deleteIndex(self,index):
        curr = self.head
        for i in range(index-2):
            curr = curr.next
        curr.next = curr.next.next
l1=LinkedList()
l1.insertBegin(60)
l1.insertBegin(50)
l1.insertBegin(40)
l1.insertBegin(30)
l1.insertBegin(20)
l1.insertBegin(10)
l1.insertSorted(65)
l1.NthNodefromEnd(5)
l1.middleofLL()
l1.deleteIndex(3)
l1.traverse()

        
