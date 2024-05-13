def f(n):
  res=n[0]
  for i in range(1,len(n)):
    if n[i] > res:
      res=n[i]
  return res 
for i in range(int(input())):
  l=list(map(int,input().split()))
  print(f(l))
