
from collections import deque
q=deque()
q.append(20)
q.append(5)
q.append(12)
q.append(7)
q.append(6)
print(q)

def rev(q):
    if len(q)==0:
        return
    x=q[0]
    q.popleft()
    rev(q)
    q.append(x)
rev(q)
print(q)
