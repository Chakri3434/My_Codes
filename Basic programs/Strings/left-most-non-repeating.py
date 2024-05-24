def f(s):
    res=float('-inf')
    count=[-1 for i in range(26)]
    for i in range(len(s)):
        index=count[ord(s[i])-ord('a')]
        if index==-1:
            index=i 
        else:
            index=-2
    for i in range(len(count)):
        if count[i]>=0:
            res=min(res,count[i])
    return -1 if  res==float('-inf') else res
print(f('abbcbda'))
