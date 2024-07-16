# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        null=[]
        curr=root
        while curr or null:
            while curr:
                null.append(curr)
                curr=curr.left
            curr=null.pop()
            res.append(curr.val)
            curr=curr.right
        return res
