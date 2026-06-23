# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        ans = True
        def dfs(node):
            nonlocal ans
            if not node:
                return 0
            lheight = dfs(node.left)
            rheight = dfs(node.right)
            if rheight - lheight > 1 or lheight - rheight > 1:
                ans = False
            return 1 + max(lheight, rheight)
        dfs(root)
        return ans