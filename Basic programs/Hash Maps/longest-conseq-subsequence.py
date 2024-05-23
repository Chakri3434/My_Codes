def f(l):
    d=[item for item in l]
    res=0
    for i in range(len(l)):
        if l[i]-1 not in d:
            curr=1 
            while l[i]+curr in d:
                curr+=1 
            res=max(res,curr)
    return res
l=[1,9,3,4,2,20]
print(f(l))
