def f(l,k):
    s=[]
    preSum=0
    for i in range(len(l)):
        preSum+=l[i]
        if preSum-k in s:
            return True
        if preSum==k:
            return True
        s.append(preSum)
    return False
l=[5,8,6,13,3,-1]
print(f(l,22))
