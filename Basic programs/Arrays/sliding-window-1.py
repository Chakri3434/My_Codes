# given an array of integers and k find the max. sum of k consequetive elemnets

def f(l,k):
  total=sum(l[:k])
  max_total=total
  
  for i in range(len(l)-k):
    total-=l[i]
    toatl+=l[i+k]
    max_total=max(max_total,total)

return max_total
