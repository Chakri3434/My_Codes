#Brian-Kerningham's Algorithm

def count_setbits(n):
  c=0
  while(n>0):
    n=n&(n-1) 
    c+=1
  print(c)
for i in range(int(input())):
  n=int(input())
  count_setbits(n)
