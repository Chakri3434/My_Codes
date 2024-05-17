#print the longest even-odd alternative appeared length in the given in array.

def f(l):
    res,curr=1,1
    for i in range(1,len(l)):
        if (l[i]%2==0 and l[i-1]%2!=0) or (l[i]%2!=0 and l[i-1]%2==0):
            curr+=1 
            res=max(res,curr)
    return res

p=list(map(int,input().split()))
print(f(p))
