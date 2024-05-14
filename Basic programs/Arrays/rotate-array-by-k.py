def f(l,k):
    for i in range(k):
        temp=l[0]
        for j in range(len(l)-1):
            l[j]=l[j+1]
        l[-1]=temp
    return l
p=list(map(int,input().split()))
k=int(input())
print(f(p,k))
