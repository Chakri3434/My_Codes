s='+*523'
stack=[]
cal=0
i=len(s)-1
while i>=0:
    if s[i]!='+' and s[i]!='-' and s[i]!='*' and s[i]!='/' and s[i]!='^':
        stack.append(s[i])
    else:
        op1=str(stack.pop())
        op2=str(stack.pop())
        cal=op1+s[i]+op2
        cal=eval(cal)
        stack.append(cal)
    i-=1
print(cal)
