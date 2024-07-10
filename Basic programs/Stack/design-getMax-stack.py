class MaxStack:

    def __init__(self):
        self.s=[]
        self.max=0

    def push(self, val: int) -> None:
        if self.s==[]:
            self.max=val
            self.s.append(val)
        elif val>=self.max:
            self.s.append(2*val-self.max)
            self.max = val
        else:
            self.s.append(val)

    def pop(self) -> None:
        if self.s[-1]>=self.max:
            self.max=2*self.max-self.s[-1]
        self.s.pop()

    def top(self) -> int:
        if self.s[-1]>=self.max:
            return self.max
        return self.s[-1]

    def getMin(self) -> int:
        return self.max

s=MaxStack()
s.push(5)
s.push(1)
s.push(7)
s.push(4)
s.push(-1)
s.push(6)
s.push(-3)
s.push(6)
s.pop()
s.pop()
s.pop()
s.pop()
print(s.top())
print(s.getMin())
