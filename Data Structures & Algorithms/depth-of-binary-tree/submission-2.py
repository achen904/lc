# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #the depth of binary tree is at root is the 1 + depth of the larger depth between its 2 child nodes. in example 1 3 is the larger one depth child. 
        #we can use recursion to find the larger depth child

        #create a dfs method where dfs returns the depth of the tree rooted at the input node. for a recursive method we need a base case, here if node is none then we return 0. then we call dfs on the left and right child to see its depths then return the max + 1.

        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            return 1 + max(left,right)
        return dfs(root)