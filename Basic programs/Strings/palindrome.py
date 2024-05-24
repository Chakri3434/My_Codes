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

#using recursions

def pal(n):
  p=n.lower()
  if p=='':
    return True
  elif p[0]==p[-1]:
    return pal(p[1:len(p)-1])
  else:
    return False
print(pal(input()))
