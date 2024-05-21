def f(l):
    d={}
    for i in range(len(l)):
        if l[i] in d:
            d[l[i]]+=1 
        else:
            d[l[i]]=1 
    for k,v in d.items():
        print(k,v)
l=[2,2,2,3,4,5,5,6]
f(l)
