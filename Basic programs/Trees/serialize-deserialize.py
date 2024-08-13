# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return 'None'
        tree_left=self.serialize(root.left)
        tree_right=self.serialize(root.right)
        return str(root.val)+','+tree_left+','+tree_right
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        tree_list=data.split(',')
        def dfs():
            node_next=tree_list.pop(0)
            if node_next == 'None':
                return None
            node_new=TreeNode(int(node_next))
            node_new.left=dfs()
            node_new.right=dfs()
            return node_new
        return dfs()
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
