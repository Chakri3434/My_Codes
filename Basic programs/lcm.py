def lcm(a,b):
  t=max(a,b)
  while True:
    if t%a==0 and t%b==0:
      return(t)
    else:
      t+=1
  return(t)
for i in range(int(input())):
  a,b=map(int,input().split())
  print(lcm(a,b))