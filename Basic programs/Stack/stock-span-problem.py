nums=[60,10,20,40,35,30,50,70,65]
s=[]
s.append(1)
print(1)
for i in range(len(nums)):
    while s and nums[s[-1]]<=nums[i]:
        s.pop()
    if not s:
        span = i+1
    else:
        span = i-s[-1]
    print(span)
    s.append(i)
