class Deque:
    
    def __init__(self,k):
        self.s=[]
        self.size=0
        self.cap=k
        
    def isFull(self):
        return self.size==self.cap
    
    def isEmpty(self):
        return self.size==0
        
    def insertFront(self,val):
        if not self.isFull():
            self.s.append(-1)
            self.size+=1
            i=self.size-1
            while i>0:
                self.s[i]=self.s[i-1]
                i-=1
            self.s[0]=val
    
    def insertRear(self,val):
        if not self.isFull():
            self.s.append(val)
            self.size+=1
        
    def deleteFront(self):
        if not self.isEmpty():
            for i in range(len(self.s)-1):
                self.s[i]=self.s[i+1]
            self.s.pop()
            self.size-=1
        
    def deleteRear(self):
        if not self.isEmpty():
            self.s.pop()
            self.size-=1
        
    def size(self):
        print(self.size)
    
    def getFront(self):
        if not self.isEmpty():
            print(self.s[0])
    
    def getRear(self):
        if not self.isEmpty():
            print(self.s[-1])
            
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
