from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q=deque()
        res=[]
        for i in range(k):
            while q and nums[i]>=nums[q[-1]]:
                q.pop()
            q.append(i)
        for i in range(k,len(nums)):
            res.append(nums[q[0]])
            while q and q[0]<=(i-k):
                q.popleft()
            while q and nums[i]>=nums[q[-1]]:
                q.pop()
            q.append(i)
        res.append(nums[q[0]])
        return res
