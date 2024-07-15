class Deque:
    
    def __init__(self,k):
        self.s=[-1]*k
        self.size=0
        self.cap=k
        self.front=0
        
    def isFull(self):
        return self.size==self.cap
    
    def isEmpty(self):
        return self.size==0
        
    def insertFront(self,val):
        if self.isFull():
            print('Deque is Full!')
        else:
            self.front=(self.front+self.cap-1)%self.cap
            self.s[self.front]=val
            self.size+=1
    
    def insertRear(self,val):
        if self.isFull():
            print('Deque is Full!')
        else:
            rear=(self.front+self.size-1)%self.cap
            rear=(rear+1)%self.cap
            self.s[rear]=val
            self.size+=1
        
    def deleteFront(self):
        if self.isEmpty():
            print('Deque is Empty!')
        else:
            self.front=(self.front+1)%self.cap
            self.size-=1
        
    def deleteRear(self):
        if self.isEmpty():
            print('Deque is Empty!')
        else:
            self.rear=(self.rear-1+self.cap)%self.cap
            self.size-=1
        
    def size(self):
        print(self.size)
    
    def getFront(self):
        if not self.isEmpty():
            print(self.s[self.front])
    
    def getRear(self):
        if not self.isEmpty():
            print(self.s[(self.front+self.size-1)%self.cap])
            
q=Deque(5)
q.insertRear(10)
q.insertFront(20)
q.insertRear(30)
q.insertFront(40)
q.getFront()
q.getRear()
print(q.isFull())
q.insertFront(50)
q.getFront()
print(q.isFull())
q.insertFront(60)
q.getFront()
