#naive 
def f(l):
    res=l[1]-l[0]
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            res=max(l[j]-l[i],res)
    return res
p=list(map(int,input().split()))
print(f(p))

#efficient
def f(l):
  res=l[1]-l[0]
  minVal=l[0]
  for i in range(len(l)):
    res=max(res,l[i]-minVal)
    minVal=min(minVal,l[i])
  return res
p=list(map(int,input().split()))
print(f(p)
