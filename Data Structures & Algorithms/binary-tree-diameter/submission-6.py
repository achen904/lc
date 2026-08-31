# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #diameter is given by height of left side + height of right side
        #use dfs to find heights of both sides
        #dfs returns the height 
        #we then use the dfs to update our ans
        ans = 0

        def dfs(node):
            nonlocal ans
            if not node:
                return 0
            left =dfs(node.left)
            right = dfs(node.right)
            ans = max(ans, left + right)
            return 1 + max(left, right) #height is given by larger height of left and right child + 1
        dfs(root)
        return ans