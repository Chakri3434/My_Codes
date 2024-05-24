def f(l):
    count=[0 for i in range(26)]
    for i in range(len(l)):
        count[ord(l[i])-ord('a')]+=1 
    for i in range(len(count)):
        if count[i]!=0:
            print(chr(i + ord('a')),count[i])
l='geeksforgeeks'
f(l)
