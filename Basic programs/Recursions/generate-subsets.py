def sub_sets(s,curr='',i=0):
  if i==len(s):
    print(curr)
    return
  sub_sets(s,curr,i+1)
  sub_sets(s,curr+s[i],i+1)
for i in range(int(input())):
  sub_sets(input())