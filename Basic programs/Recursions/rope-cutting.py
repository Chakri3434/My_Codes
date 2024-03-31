#given a rope of length n, and cuts a,b,c applied. 
#find the max number of cuts that can be made on the rope. 
#if exact cuts can't be made, return 0
#e.g i/p : 5  (2,5,1)
#    o/p : 5 (cut of 1 can be made 5 times to completely cut the rope.)

def rope(n,a,b,c):
  if n==0 :
    return 0
  if n<0 :
    return -1
  res=max(rope(n-a,a,b,c),
          rope(n-b,a,b,c),
          rope(n-c,a,b,c))
  if res==-1:
    return -1
  else:
    return res+1

for i in range(int(input())):
  n,a,b,c=map(int,input().split())
  print(rope(n,a,b,c))