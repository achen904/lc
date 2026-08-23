# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        index = {}
        for ind, value in enumerate(inorder):
            index[value] = ind
        preindex = 0
        def dfs(l, r):
            nonlocal preindex
            if l > r:
                return None
            m = index[preorder[preindex]]
            root = TreeNode(preorder[preindex])
            preindex += 1
            root.left = dfs(l, m - 1)
            root.right = dfs(m + 1, r)

            return root
        return dfs(0, len(preorder) - 1)
            
            
            