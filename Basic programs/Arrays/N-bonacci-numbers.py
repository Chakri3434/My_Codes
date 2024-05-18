#print first m N-bonacci numbers

def f(n,m):
    l=[ 0 for i in range(n-1)]
    l.append(1)
    s=0
    for e in range(n-1,m-1):
        l.append(sum(l[s:e+1]))
        s+=1 
    return l
n,m=map(int,input().split())
print(f(n,m))
