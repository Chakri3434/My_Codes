# a leader is an element for which the right elements of the leader are less than this element.

def f(l):
    temp=l[-1]
    p=[temp]
    i=len(l)-1
    while i>0:
        if l[i-1]>temp:
            p.insert(0,l[i-1])
            temp=l[i-1]
        i-=1
    return p
k=list(map(int,input().split()))
print(f(k))
