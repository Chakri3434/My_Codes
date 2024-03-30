def printnum(n):
  if n==0:
    return
  printnum(n-1)
  print(n)
for i in range(int(input())):
  n=int(input())
  print(printnum(n))
