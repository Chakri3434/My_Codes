def f(l,k):
    
    d={}
    
    for i in range(k):
        if l[i] in d:
            d[l[i]]+=1 
        else:
            d[l[i]]=1
        
    print(len(d))
    
    for i in range(k,len(l)):
        d[l[i-k]]-=1 
        if d[l[i-k]]==0:
            d.pop(l[i-k])
        
        if l[i] in d:
            d[l[i]]+=1 
        else:
            d[l[i]]=1 
            
        print(len(d))
            
f([2,2,3,4,5,5,5,4,5,4],4)
