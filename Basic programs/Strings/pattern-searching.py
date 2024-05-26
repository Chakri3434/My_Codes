def f(s,p):
    n=len(s)
    k=len(p)
    for i in range(n-k+1):
        if s[i:i+k]==p:
            print(i)
f('geeksforgeeks','eks')
