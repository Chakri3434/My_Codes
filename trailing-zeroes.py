def zeroes(n):
  i=1
  res=0
  temp=n
  while(temp!=0):
    temp=(n//pow(5,i))
    res+=temp
    i+=1
  print(res)
for i in range(int(input())):
  n=int(input())
  zeroes(n)