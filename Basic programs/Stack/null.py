def bracket(s):
    null=[]
    for i in range(len(s)):
        tmp=s
        if s[i] == '+' :
            if null==[]:
                null.append(s[i])
            else:
                s=tmp[:i-3]+'('+tmp[i-3:i]+ ')' +tmp[i:]
        elif s[i] == '-':
            if null==[]:
                null.append(s[i])
            else:
                s=tmp[:i-3]+'('+tmp[i-3:i]+ ')' +tmp[i:]
        elif s[i]=='*':
            if null==[]:
                null.append(s[i])
            else:
                s=tmp[:i-1] +'('+ tmp[i-1:i+2] +')'+ tmp[i-2:]
        print(s)
    return s 
print(bracket('a+b*c'))
                
            
