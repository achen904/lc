# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def recur(node):
            if not node:
                return
            temp = node.left
            node.left = recur(node.right)
            node.right = recur(temp)
            return node
        
        return recur(root)
        