def f(l,k):
    d={}
    n=len(l)
    
    for i in range(len(l)):
        if l[i] in d:
            d[l[i]]+=1 
        elif len(d) < k-1 :
            d[l[i]]=1 
        else:
            p=[]
            for key in d.keys():
                d[key]-=1 
                if d[key]==0:
                    p.append(key)
            for i in range(len(p)):
                d.pop(p[i])
    for t,v in d.items():
        if v>(n/k):
            print(t)
f([30,10,20,20,20,10,40,30,30],4)
