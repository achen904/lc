# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        #diamter of a binary tree equals = longest path btwn any 2 nodes
        #which also eqauls the left trees max depth + right trees max depth for any node. 
        #we want dfs(node) to return the maximum depth starting at node
        def dfs(node):
            if not node:
                return 0 #empty node = no distance
            nonlocal ans
            left = dfs(node.left)  #finds the max depth of left
            right = dfs(node.right) #finds max depth of right
            ans = max(ans, left + right) #diameter is updated to be the max of sum
            return 1 + max(left, right) #if no children, then max depth 1, otherwise max is 1 + the larger depth between left and right
        dfs(root)
        return ans