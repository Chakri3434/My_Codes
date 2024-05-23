def f(l):
    s=set()
    preSum=0
    for i in range(len(l)):
        preSum+=l[i]
        if preSum==0:
            return True
        if preSum in s:
            return True
        s.add(preSum)
    return False
l=[1,4,13,-3,-10,5]
print(f(l))
