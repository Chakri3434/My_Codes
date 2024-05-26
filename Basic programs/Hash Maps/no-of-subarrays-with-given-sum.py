def subarraySum(nums, k):
    preSum=0
    d={}
    c=0
    for i in range(len(nums)):
        preSum+=nums[i]
        if preSum==k:
            c+=1
        if preSum-k in d:
            c+=d[preSum-k]
        if preSum in d:
            d[preSum]+=1
        else:
            d[preSum]=1
    return c
