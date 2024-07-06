# NAIVE METHOD

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res=0
        for i in range(len(heights)):
            curr = heights[i]
            j=i-1
            while j>=0:
                if heights[j]>=heights[i]:
                    curr += heights[i]
                    j-=1
                else:
                    break
            j=i+1
            while j<len(heights):
                if heights[j]>=heights[i]:
                    curr += heights[i]
                    j+=1
                else:
                    break
            res=max(res,curr)
        return res

# Better O(n)

class Solution:
    def largestRectangleArea(self, nums: List[int]) -> int:
        ps=[]
        ps.append(-1)
        istack=[]
        istack.append(0)
        for i in range(1,len(nums)):
            while istack and nums[istack[-1]]>=nums[i]:
                istack.pop()
            if not istack:
                ps.append(-1)
            else:
                ps.append(istack[-1])
            istack.append(i)
        istack=[]
        ns=[0]*len(nums)
        ns[-1]=len(nums)
        i = len(nums)-2
        istack.append(len(nums)-1)
        while i>=0:
            while istack and nums[istack[-1]]>=nums[i]:
                istack.pop()
            if not istack:
                ns[i]=len(nums)
            else:
                ns[i]=istack[-1]
            istack.append(i)
            i-=1 
        print(ns)
        res=0
        for i in range(len(nums)):
            curr=nums[i]
            curr+=(i-ps[i]-1)*nums[i]
            curr+=(ns[i]-i-1)*nums[i]
            res=max(res,curr)
        return res

#BEST O(n) Single Traversal

nums=[6,2,5,4,1,5,6]
res=0
s=[]
for i in range(len(nums)):
    while s and nums[s[-1]]>=nums[i]:
        tp=s.pop()
        curr = nums[tp]*(i if not s else (i-s[-1]-1))
        res = max(res,curr)
    s.append(i)
while s:
    tp = s.pop()
    curr = nums[tp]*(len(nums) if not s else (len(nums)-s[-1]-1))
    res = max(res,curr)
print(res)

