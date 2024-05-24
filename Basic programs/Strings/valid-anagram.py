def f(s1,s2):
    count=[0 for i in range(26)]
    for i in range(len(s1)):
        count[(ord(s1[i]) - ord('a'))]+=1 
        count[(ord(s2[i]) - ord('a'))]-=1 
    for i in range(len(count)):
        if count[i]!=0:
            return False
    return True
print(f('abcd','dccb'))
