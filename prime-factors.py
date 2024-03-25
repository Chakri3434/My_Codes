def prime(n):
  if n==1:
    return False
  if n==2 or n==3:
    return True
  if n%2==0 or n%3==0:
    return False
  for i in range(5,int(n**0.5)+1,6):
    if n%i==0 or n%(i+2)==0:
      return False
  return True
p=int(input())
for i in range(1,p):
  if p%i==0:
    if prime(i):
      temp=i
      while(p%temp==0):
        print(i)
        temp*=i

