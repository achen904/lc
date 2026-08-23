# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = root.val

        def dfs(node): #returns the max sum path going through node
            nonlocal ans
            if not node:
                return 0
            left = max(dfs(node.left), 0) #put 0 because if it is negative we don't want to use that side
            right = max(dfs(node.right), 0)
            ans = max(ans, left + right + node.val)
            return node.val + max(left, right) #can only go down either the left or right path not both or else won't be considered a path
        dfs(root)
        return ans