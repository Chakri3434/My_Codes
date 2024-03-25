def hcf(a,b):
  if b==0:
    return a
  else:
    return hcf(b,a%b)
for i in range(int(input())):
  a,b=map(int,input().split())
  print(hcf(a,b))