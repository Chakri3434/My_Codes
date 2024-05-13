def f(a):
  s,e=0,len(a)-1
  while s<e:
    temp=a[e]
    a[e]=a[s]
    a[s]=temp
    s+=1
    e-=1
  return a
for i in range(int(input())):
  n=list(map(int,input().split()))
  print(f(n))
