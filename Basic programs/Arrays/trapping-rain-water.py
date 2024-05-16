def f(a):
    res=0
    
    lmax=[a[0]]
    for i in range(1,len(a)):
        lmax.append(max(a[i],lmax[i-1]))
    
    rmax=[0 for i in range(len(a))]
    j=len(a)-2
    rmax[-1]=a[-1]
    while j>=0:
        rmax[j]=max(a[j],rmax[j+1])
        j-=1
    
    for i in range(1,len(a)-1):
        res+=(min(lmax[i],rmax[i])-a[i])
    
    return res
l=list(map(int,input().split()))
print(f(l))
