# move 1 disc at a time
# no larger disc above smaller
# only top discs can be moved
# n is number of discs
# a is initial position
# b is auxilary position
# c is final destination
#give instructions to move the discs

def toh(n,a,b,c):
  if n==1:
    print('move disc 1 from A to C')
    return
  toh(n-1,a,c,b)
  print('move disc '+str(n)+' from A to C')
  toh(n-1,b,a,c)
for i in range(int(input())):
  n=int(input())
  toh(n,a,b,c)
