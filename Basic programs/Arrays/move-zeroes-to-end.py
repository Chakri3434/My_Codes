def f(l):
    for i in range(len(l)):
        if l[i]==0:
            l.remove(l[i])
            l.append(0)
    return l 
p=list(map(int,input().split()))
print(f(p))
