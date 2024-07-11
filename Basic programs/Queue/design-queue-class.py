class Queue:
    def __init__(self):
        self.q=[]
        self.e=0
    def enque(self,data):
        if self.q==[]:
            self.q.append(data)
        else:
            self.q.append(data)
            self.e+=1 
    def deque(self):
        if self.q==[]:
            print('queue is empty!')
        else:
            for i in range(len(self.q)-1):
                self.q[i]=self.q[i+1]
            self.q.pop()
            self.e-=1 
    def front(self):
        if self.q==[]:
            print('queue is empty!')
        else:
            print(self.q[0])
    def rear(self):
        if self.q==[]:
            print('queue is empty!')
        else:
            print(self.q[self.e])
    def length(self):
        print(len(self.q))
q=Queue()
q.enque(50)
q.enque(30)
q.enque(20)
q.enque(40)
q.deque()
q.deque()
q.front()
q.deque()
q.front()
q.rear()
q.length()
