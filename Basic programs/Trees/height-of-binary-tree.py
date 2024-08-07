# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        st=[root]
        c=0
        while st:
            tmp=st
            st=[]
            for node in tmp:
                if node.left:
                    st.append(node.left)
                if node.right:
                    st.append(node.right)
            c+=1
        return c


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root==None:
            return 0
        return 1+max(self.maxDepth(root.left),self.maxDepth(root.right))

