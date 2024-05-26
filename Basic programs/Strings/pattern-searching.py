#Naive :
def f(s,p):
    n=len(s)
    k=len(p)
    for i in range(n-k+1):
        if s[i:i+k]==p:
            print(i)
f('geeksforgeeks','eks')

#Improved Naive for distinct characters:
def f(s,p):
    n=len(s)
    k=len(p)
    i=0
    while i<=n-k:
        for j in range(k):
            if p[j]!=s[i+j]:
                break
        if j==k:
            print(i)
        if j==0:
            i+=1 
        else:
            i+=j
f('abcabcd','abcd')
