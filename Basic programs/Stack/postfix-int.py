s='52*3+'
stack=[]
cal=0
for i in range(0,len(s)):
    if s[i]!='+' and s[i]!='-' and s[i]!='*' and s[i]!='/' and s[i]!='^':
        stack.append(s[i])
    else:
        op1=str(stack.pop())
        op2=str(stack.pop())
        cal=op1+s[i]+op2
        cal=eval(cal)
        stack.append(cal)
print(cal)
