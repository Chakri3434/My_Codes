from collections import deque
q=deque()
def insertMin(q,val):
    q.append(val)
    print(q)
def insertMax(q,val):
    q.appendleft(val)
    print(q)
def getMin(q):
    print(q.pop())
def getMax(q):
    print(q.popleft())
insertMin(q,4)
insertMin(q,3)
insertMin(q,2)
insertMin(q,1)
insertMax(q,34)
insertMax(q,46)
insertMax(q,77)
getMax(q)
getMax(q)
getMin(q)
getMin(q)
