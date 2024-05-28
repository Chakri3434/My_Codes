def f(txt,pat):
    n=len(txt)
    m=len(pat)
    p,t,h=0,0,1
    d=5
    q=89 #choose q as a big primenumber so that problem simplifies for bigger strings

    #calculate (d^(m-1))%q
    for i in range(1,m):
        h=(h*d)%q
      
    #calculate p and t0
    for i in range(m):
        p=(p*d + ord(pat[i]))%q
        t=(t*d + ord(txt[i]))%q

    for i in range(n-m):
        #check for spurious hits
        if p==t:
            flag=True
            for j in range(m):
                if txt[i+j]!=pat[i]:
                    flag=False
                    break
            if flag:
                print(i)
        #roll the hash
        if i<(n-m):
            t=((d*(t-ord(txt[i])*h))+ord(txt[i+m]))%q
            if t<q:
                t+=q
    
print(f('abcabcd','abcd'))
