def f(l1,l2):
    s1=set(l1)
    s2=set(l2)
    union_set=s1.union(s2)
    return len(union_set)
l1=[10,15,20,15,30,30,5]
l2=[30,5,30,80]
print(f(l1,l2))
