def f(l):
    s=[]
    preSum=0
    for i in range(len(l)):
        preSum+=l[i]
        if preSum in s:
            return True
        if preSum==0:
            return True
        s.append(preSum)
    return False
l=[1,4,13,-3,-10,5]
print(f(l))
