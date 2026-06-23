# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def method(node):
            if not node:
                return 0
            return max(1 + method(node.left), 1 + method(node.right))

        return method(root)
        