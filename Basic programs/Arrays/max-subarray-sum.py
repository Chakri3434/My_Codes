# naive : O(n^2)
def f(l):
    res=l[0]
    for i in range(len(l)):
        curr=0
        for j in range(i,len(l)):
            curr+=l[i]
            res=max(res,curr)
    return res

# efficient : O(n)
# Kadane's Algorithm
def f(l):
    res=l[0]
    maxEnding=l[0]
    for i in range(1,len(l)):
        maxEnding=max(maxEnding+l[i],l[i])
        res=max(res,maxEnding)
    return res
