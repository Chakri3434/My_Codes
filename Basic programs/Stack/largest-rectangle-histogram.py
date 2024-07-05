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
