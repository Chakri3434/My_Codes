#remove the duplicates from the array
#replace them with underscores at the end for each repeated element

def f(l):
    temp=len(l)
    p=set(l)
    l.clear()
    for item in p:
        l.append(item)
    for i in range(len(p)+1,temp):
        l.append('_')
    return l 
l=list(map(int,input().split()))
print(f(l))
