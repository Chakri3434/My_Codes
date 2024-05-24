#using strings

def f(l):
    count=[0 for i in range(26)]
    for i in range(len(l)):
        count[ord(l[i])-ord('a')]+=1 
    for i in range(len(count)):
        if count[i]!=0:
            print(chr(i + ord('a')),count[i])
l='geeksforgeeks'
f(l)

#using hashmap

def f(l):
    d={}
    for i in range(len(l)):
        if l[i] in d:
            d[l[i]]+=1 
        else:
            d[l[i]]=1 
    q=[(k,v) for k,v in d.items()]
    q.sort(key= lambda x:x[0])
    print(q)
l='geeksforgeeks'
f(l)
