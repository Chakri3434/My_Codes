# NAIVE------------------->

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        d1=self.height(root.left)+self.height(root.right)
        d2=self.diameterOfBinaryTree(root.left)
        d3=self.diameterOfBinaryTree(root.right)
        return max(d1,max(d2,d3))
    def height(self,root):
        if not root:
            return 0
        return 1+max(self.height(root.left),self.height(root.right))


# EFFICIENT --------------------->

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res=0
        def dfs(node):
            if not node: return 0
            lh=dfs(node.left)
            rh=dfs(node.right)
            self.res=max(self.res,lh+rh)
            return max(lh,rh)+1
        dfs(root)
        return self.res
