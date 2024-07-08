# NAIVE O(n*k)
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        arr = [i for i in range(1,n+1)]
        s=0
        while len(arr)!=1:
            c=1 
            while c!=k:
                s+=1
                s=s%len(arr)
                c+=1 
            arr.pop(s)
            print(arr)
        return arr[0]


def jos(n,k):
  if n==1:
    return 0
  else:
    return (jos(n-1,k)+k)%n
for i in range(int(input())):
  n,k=map(int,input().split())
  print(jos(n,k))
