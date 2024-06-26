nums=[15,10,18,12,4,6,2,8]
s=[]
s.append(nums[0])
print(-1)
for i in range(1,len(nums)):
    while s and s[-1]<=nums[i]:
        s.pop()
    if not s:
        print(-1)
    else:
        print(s[-1])
    s.append(nums[i])
