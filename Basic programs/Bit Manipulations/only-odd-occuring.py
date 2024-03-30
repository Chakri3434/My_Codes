def only_odd_occ(l):
  res=0
  for i in range(len(l)):
    res=res^l[i]
  return res
for i in range(int(input())):
  l=list(map(int,input().split()))
  print(only_odd_occ(l))