#s1='abcd'
#s2='ad'


def f(s1,s2):
    i,j=0,0
    while i<len(s1) and j<len(s2):
        if s1[i]==s2[j]:
            i+=1 
            j+=1
        else:
            i+=1 
    return j==len(s2)
print(f('abcd','ad'))
