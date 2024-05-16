# max consequetive 1's in an binary array
def f(a):
    res=0
    curr=0
    for i in range(len(a)):
        if a[i]==0:
            curr=0
        else:
            curr+=1
            res=max(res,curr)
    return res
l=list(map(int,input().split()))
print(f(l))
