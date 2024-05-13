def f(n):
  for i in range(len(n)-1):
    if n[i+1]<n[i]:
      return False
    return True
for i in range(int(input())):
  n=list(map(int,input().split()))
  print(f(n))
