def printnum(n):
  if n==0:
    return 
  print(n)
  printnum(n-1)
for i in range(int(input())):
  n=int(input())
  print(printnum(n))