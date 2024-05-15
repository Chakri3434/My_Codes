def f(a):
    res=0
    
    lmax=[a[0]]
    for i in range(1,len(a)):
        lmax[i]=max(a[i],lmax[i-1])
        
    rmax=[a[-1]]
    j=len(l)-2
    while j>=0:
        rmax=max(a[j],rmax[j+1])
        j-=1
      
    for i in range(1,len(l)-1):
        res+=min(lmax[i],rmax[i])-a[i]
    return res
l=list(map(int,input().split()))
print(f(l))
