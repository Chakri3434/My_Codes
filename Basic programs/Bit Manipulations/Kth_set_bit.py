def Kth_set_bit(n,k):
  if ((n<<(k-1)&1)==1):
    return('yes')
  else:
    return('no')
for i in  range(int(input())):
  n,k=map(int,input().split())
  print(Kth_set_bit(n,k))