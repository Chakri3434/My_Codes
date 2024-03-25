def fact(n,k):
  if n==0:
    return k
  else:
    return fact(n-1,k*n)
for i in range(int(input())):
  n=int(input())
  print(fact(n,1))