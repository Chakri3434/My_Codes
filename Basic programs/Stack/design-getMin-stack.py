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


#  O(1) Space
class MinStack:

    def __init__(self):
        self.s=[]
        self.min=0

    def push(self, val: int) -> None:
        if self.s==[]:
            self.min=val
            self.s.append(val)
        elif val<=self.min:
            self.s.append(2*val-self.min)
            self.min = val
        else:
            self.s.append(val)

    def pop(self) -> None:
        if self.s[-1]<=self.min:
            self.min=2*self.min-self.s[-1]
        self.s.pop()

    def top(self) -> int:
        if self.s[-1]<=self.min:
            return self.min
        return self.s[-1]

    def getMin(self) -> int:
        return self.min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
