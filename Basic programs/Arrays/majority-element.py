# an element is a majority if the freq of that elemnet is greater than len(l)//2.

def f(l):
    n=len(l)//2
    d={}
    for i in range(len(l)):
        if l[i] in d:
            d[l[i]]+=1
            if d[l[i]]>n:
                return(i)
        else:
            d[l[i]]=1 
    return -1

#Moore's Voting Algorithm

def f(l):
    res=0 
    c=1 
    for i in range(1,len(l)):
        if l[res]==l[i]:
            c+=1 
        else:
            c-=1 
        if c==0:
            res=i
            c=1 
    c=0 
    for i in range(len(l)):
        if l[i]==l[res]:
            c+=1 
    if c<=len(l)//2:
        res=-1
    return res
