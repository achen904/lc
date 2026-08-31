# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        #since this is a BST, we know that if p and q are on opposite sides of a node then that node is the lca, so at a given node we must check whether p and q are both less than it or both greater than it, if one is <= and the other is >= then the current node is the lca otherwise we move to the respective node and continue
        while root:
            if p.val < root.val and q.val < root.val:
                root = root.left
            elif p.val > root.val and q.val > root.val:
                root = root.right
            else:
                return root