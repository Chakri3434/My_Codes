nums=[5,15,10,8,6,12,9,18]
s=[]
ans=[]
s.append(nums[-1])
ans.append(-1)
i=len(nums)-2
while i>=0:
    while s and s[-1]<=nums[i]:
        s.pop()
    if not s:
        ans.append(-1)
    else:
        ans.append(s[-1])
    s.append(nums[i])
    i-=1
print(ans[::-1])
