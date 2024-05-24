#using 2 pointers

def f(l):
    s,e=0,len(l)-1
    while s<e:
        if l[s]==l[e]:
            s+=1 
            e-=1 
        else:
            return False
    return True
l='grouorg'
print(f(l))
