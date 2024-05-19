def f():
    d={'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7}
    d1={v:k for k,v in d.items()}
    res='h8'
    
    l=['2l','2d','1r']
    for i in range(len(l)):
        for j in range(int(l[i][0])):
            if l[i][1]=='l':
                if res[0]!='a':
                    res[0]=str(d1[str(int(d[res[0]])-1)])
                else:
                    return -1
            elif l[i][1]=='r':
                if res[0]!='h':
                    res[0]=str(d1[str(int(d[(res[0])])+1)])
                else:
                    return -1
            elif l[i][1]=='u':
                if res[1]!='8':
                    res[1]=int(res[1])+1 
                else:
                    return -1
            elif l[i][1]=='d':
                if res[1]!='1':
                    res[1]=int(res[1])-1
                else:
                    return -1
    return res
                    
print(f())                    
    
    
# // h8
# // 3 
# // 2l 
# // 2d 
# // 1r

# //g6 
