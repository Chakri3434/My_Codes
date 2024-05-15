#given costs of a products user shoud should buy and sell the product 
#print the maximum profit
#l=[1,5,3,8,12]
#o/p: 13 ( (5-1) + (12-5) )

def f(l):
  res=0
  for i in range(1,len(l)):
    if l[i]>l[i-1]:
      res+=l[i]-l[i-1]
  return res
l=list(map(int,input().split()))
print(f(l))
