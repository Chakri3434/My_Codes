import math
def div(n):
    i=1
    while (i<math.sqrt(n)):
        if n%i==0:
            print(i)
        i+=1
    while (i>=1):
        if n%i==0:
            print(n//i)
        i-=1
div(int(input()))
