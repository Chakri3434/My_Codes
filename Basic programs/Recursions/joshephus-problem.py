def jos(n,k):
  if n==1:
    return 0
  else:
    return (jos(n-1,k)+k)%n
for i in range(int(input())):
  n,k=map(int,input().split())
  print(jos(n,k))
