class Stack:
    
    def __init__(self):
        self.ms=[]
        self.ass=[]
    
    def push(self,x):
        if self.ass==[] or self.ass[-1]>=x:
            self.ass.append(x)
        self.ms.append(x)
        
    def popp(self):
        if self.ass[-1]==self.ms[-1]:
            self.ass.pop()
        self.ms.pop()
        
    def getMin(self):
        print(self.ass[-1])
        
l=Stack()
l.push(5)
l.push(10)
l.push(4)
l.push(2)
l.push(6)
l.push(4)
l.popp()
l.popp()
l.push(2)
l.popp()
l.push(1)
l.popp()
l.popp()
l.getMin()
