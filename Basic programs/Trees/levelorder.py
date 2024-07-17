# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q=deque()
        q.append(root)
        res=[]
        while q:
            l=[]
            for _ in range(len(q)):
                tp=q.popleft()
                l.append(tp.val)
                if tp.left:
                    q.append(tp.left)
                if tp.right:
                    q.append(tp.right)
            res.append(l)
        return res
