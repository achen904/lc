# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, left, right):
            if not root:
                return True
            if not root.val < left or not root.val > right:
                return False
            l = dfs(root.left, root.val, right)
            r = dfs(root.right, left, root.val)
            return l and r
        return dfs(root, float('inf'), -float('inf'))
            

            