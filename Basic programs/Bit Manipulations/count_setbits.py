def count_setbits(n):
  c=0
  while n>0:
    if n%2!=0:
      c+=1
    n=n//2
  return c
for i in range(int(input())):
  n=int(input())
  print(count_setbits(n))
