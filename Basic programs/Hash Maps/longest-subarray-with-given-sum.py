def f(l,k):
    d={}
    preSum=0 
    res=0 
    for i in range(len(l)):
        preSum+=l[i]
        if preSum==k:
            res=i+1 
        if preSum not in d:
            d[preSum]=i 
        if preSum-k in d:
            res=max(res,i-d[preSum-k])
    return res
l=[8,3,1,5,-6,6,2,2]
print(f(l,4))
