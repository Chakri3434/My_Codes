def digitsum(n):
  if n<10:
    return n
  return n%10 + digitsum(n//10)
for i in range(int(input())):
  n=int(input())
  print(digitsum(n))