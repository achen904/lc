# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        index = {}
        for i, n in enumerate(inorder):
            index[n] = i
        preIndex = 0
        def dfs(l, r):
            if l > r:
                return None
            nonlocal preIndex
            root_val = preorder[preIndex]
            preIndex += 1
            m = index[root_val]
            root = TreeNode(root_val)
            root.left = dfs(l, m -1)
            root.right = dfs(m + 1, r)
            return root
        return dfs(0, len(preorder) - 1)
        