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
l1=linkedList()
l1.traversal()
