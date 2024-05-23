def f(l,k):
    s=set()
    preSum=0
    for i in range(len(l)):
        preSum+=l[i]
        if preSum==k:
            return True
        if (preSum-k) in s:
            return True
        s.add(preSum)
    return False
l=[5,8,6,13,3,-1]
print(f(l,22))
