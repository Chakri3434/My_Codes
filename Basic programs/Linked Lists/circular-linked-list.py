class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None
    def traverse(self):
        if self.head is None:
            print('Linked List is empty')
        else:
            curr = self.head
            while curr.next != self.head:
                print(curr.data)
                curr = curr.next
            print(curr.data)
    def addBegin(self,data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
            newnode.next = self.head
        else:
            curr = self.head
            while curr.next != self.head:
                curr = curr.next
            curr.next = newnode
            newnode.next = self.head
            self.head = newnode
cl=CircularLinkedList()
cl.addBegin(10)
cl.addBegin(20)
cl.addBegin(-30)
cl.traverse()
