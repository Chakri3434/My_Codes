def powerof2(n):
  if n<=1:
    return False
  c=0
  while n>0:
    if n%2!=0:
      c+=1
    n=n//2
  if c==1:
    return True
  return False
for i in range(int(input())):
  n=int(input())
  print(powerof2(n))