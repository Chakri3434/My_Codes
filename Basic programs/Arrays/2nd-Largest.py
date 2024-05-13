def f(n):
  l1=n[0]
  l2=n[0]
  for i in range(1,len(n)):
    if n[i]>l1:
      l2=l1
      l1=n[i]
    else:
      if n[i]<l2:
        l2=n[i]
  if l1==l2:
    return -1
  return l2
for i in range(int(input())):
  n=list(map(int,input().split()))
  print(f(n))
