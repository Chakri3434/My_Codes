def normal_sum(l):
    res=l[0]
    maxEnding=l[0]
    for i in range(1,len(l)):
        maxEnding=max(maxEnding+l[i],l[i])
        res=max(res,maxEnding)
    return res

def circular_sum(l):
    max_normal=normal_sum(l)
    
    if max_normal < 0:
        return max_normal
    
    arr_sum=0
    
    for i in range(len(l)):
        arr_sum+=l[i]
        l[i]=-l[i]
        
    max_circular= arr_sum + normal_sum(l)
    
    return max(max_normal,max_circular)
