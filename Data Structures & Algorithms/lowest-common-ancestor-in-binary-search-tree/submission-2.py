# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        #if p and q are on different sides of current node than the current node is the lowest common ancestor
        #otherwise if p and q are < then we traverse left
        #if p and q are b > then we traverse right

        def dfs(node):
            if p.val < node.val and q.val < node.val:
                return dfs(node.left)
            if p.val > node.val and q.val > node.val:
                return dfs(node.right)
            return node
        return dfs(root)
