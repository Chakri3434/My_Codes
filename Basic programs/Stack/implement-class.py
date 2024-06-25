class myStack:
    def  __init__(self,data):
        self.s=[data]
        self.size = 1 
    def push(self,data):
        self.s.append(data)
        self.size+=1 
        print(self.s)
    def peek(self):
        if self.size:
            print(self.s[-1])
        else:
            print('Stack is empty')
    def popp(self):
        if self.size:
            self.s.pop()
            self.size-=1 
            print(self.s)
        else:
            print('Stack is empty')
    def isEmpty(self):
        if self.size:
            print('true')
        else:
            print('false')
    def sizze(self):
        print(self.size)
s1=myStack(10)
s1.push(5)
s1.push(15)
s1.push(25)
s1.peek()
s1.popp()
s1.push(35)
s1.sizze()
s1.isEmpty()
        
