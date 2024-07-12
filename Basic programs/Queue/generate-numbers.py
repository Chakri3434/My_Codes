# Generate first n numbers with the digits {5,6}
from collections import deque

q=deque()
n=10
q.append('5')
q.append('6')
for i in range(n):
    tp=q.popleft()
    print(tp)
    q.append(tp+'5')
    q.append(tp+'6')
