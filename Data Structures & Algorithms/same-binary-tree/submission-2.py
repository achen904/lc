# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def helper(p, q):
            if not p and not q:
                return True
            elif not p or not q:
                return False
            else:
                if p and q and p.val == q.val:
                    l = helper(p.left, q.left)
                    r = helper(p.right, q.right)
                    if l and r:
                        return True
                return False
        return helper(p, q)

