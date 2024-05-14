def f(l):
    d={}
    for i in range(len(l)):
        if l[i] in d:
            d[l[i]]+=1 
        else:
            d[l[i]]=1 
    l=[(k,v) for k,v in d.items()]
    return l
p=list(map(int,input().split()))
print(f(p))
