def f(l1,l2):
    s=set(l1)
    c=0
    for i in range(len(l2)):
        if l2[i] in s:
            c+=1 
            s.remove(l2[i])
    return c
l1=[10,15,20,15,30,30,5]
l2=[30,5,30,80]
print(f(l1,l2))
