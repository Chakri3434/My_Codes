def two_odd_occ(l):
  xor=0
  res1=0
  res2=0
  for i in range(len(l)):
    xor=xor^l[i]
  xor=xor&(~(xor-1)) #finding right most set bit
  for i in range(len(l)):
    if l[i]&xor==1:
      res1=res1^l[i]
    else:
      res2=res2^l[i]
  return(res1,res2)

for i in range(int(input())):
  l=list(map(int,input().split()))
  print(two_odd_occ(l))
