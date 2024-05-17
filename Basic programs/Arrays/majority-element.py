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
