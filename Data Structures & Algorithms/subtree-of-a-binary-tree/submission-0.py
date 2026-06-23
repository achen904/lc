# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sameTree(t1, t2):
            if not t1 and not t2:
                return True
            else:
                if t1 and t2 and t1.val == t2.val:
                    l = sameTree(t1.left, t2.left)
                    r = sameTree(t1.right, t2.right)
                    if l and r:
                        return True
                return False
        ans = False
        def dfs(root):
            if not root:
                return
            if root.val == subRoot.val:
                if sameTree(root, subRoot):
                    nonlocal ans
                    ans = True
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return ans
            