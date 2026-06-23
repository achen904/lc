# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def height(node):
            if not node:
                return 0
            left = 1 + height(node.left)
            right = 1 + height(node.right)
            return max(left, right)
        def helper(node):
            if not node:
                return 0
            leftHeight = height(node.left)
            rightHeight = height(node.right)
            leftDiameter = helper(node.left)
            rightDiameter = helper(node.right)
            nonlocal ans
            ans = max(ans, leftDiameter, rightDiameter, leftHeight + rightHeight)
            return ans
        return helper(root)