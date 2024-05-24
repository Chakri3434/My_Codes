def f(s):
    res=float('inf')
    count=[-1 for i in range(26)]
    for i in range(len(s)):
        if count[ord(s[i])-ord('a')]==-1:
            count[ord(s[i])-ord('a')]=i 
        else:
            res=min(res,count[ord(s[i])-ord('a')])
    return -1 if  res==float('inf') else res
print(f('gekskforeeks'))
            
