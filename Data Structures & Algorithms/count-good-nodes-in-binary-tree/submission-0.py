# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans = 0
        def dfs(root, big):
            if not root:
                return 
            nonlocal ans
            if root.val >= big:
                ans += 1
            dfs(root.left, max(big, root.val))
            dfs(root.right, max(big, root.val))
        dfs(root, root.val)
        return ans