# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        #max path sum at a node is the node.val + max(left path) + max(right path)
        #if we use dfs we return either the max path going down the left side or the max path going down the right side, if we return the max path of the node in general, it returns going down a v shape however the final path cannot split/visit a single node twice
        ans = root.val
        def dfs(node):
            nonlocal ans
            if not node:
                return 0
            left = max(dfs(node.left),0) #either use the left side or not if it is less than 0
            right = max(dfs(node.right), 0)
            ans = max(ans, node.val + left + right)
            return max(left, right) + node.val #we must use node.val however we can only go down one path, not both, however if the final ans goes down both paths then the node.val is the root
        dfs(root)
        return ans