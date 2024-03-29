def div(n):
  for i in range(1,int(n**0.5)+1):
    if n%i==0:
      print(i)
      print(n//i)
for i in range(int(input())):
  n=int(input())
  div(n)
