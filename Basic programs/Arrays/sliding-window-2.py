#given unsorted arry of non-negative int
#find if there is a subarry with given sum

def(l,summ):
  s=0
  res=l[0]
  for e in range(1,len(l)):
    res+=l[e]

  while res>summ:
    res-=l[s]
    s-=1
  return res==sum
