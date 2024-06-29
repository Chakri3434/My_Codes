# NAIVE SOLUTION 
nums=[6,2,5,4,1,5,6]
res=0
for i in range(len(nums)):
    curr = nums[i]
    j=i-1
    while j>=0 :
        if nums[j]>=nums[i]:
            curr += nums[i]
            j-=1
        else:
            break
    j=i+1 
    while j<len(nums):
        if nums[j]>=nums[i]:
            curr+=nums[i]
            j+=1
        else:
            break
    res=max(res,curr)
print(res)
