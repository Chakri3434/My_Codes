def f(l):
    for i in range(len(l)):
        if l[i]==0:
            l[i]=-1
    preSum,res=0,0
    d={}
    for i in range(len(l)):
        preSum+=l[i]
        if preSum==0:
            res=i+1 
        if preSum not in d:
            d[preSum]=i 
        if preSum in d:
            res=max(res,i-d[preSum])
    return res
l=[1,0,1,1,1,0,0]
print(f(l))
