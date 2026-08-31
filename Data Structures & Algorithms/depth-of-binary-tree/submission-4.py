# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #iterative solution
        #must store state along with the node, the state here is the depth at the current node

        stack = []
        #initialize the stack with the root node, it has depth 1 if not none
        if root:
            stack.append((root, 1))
        else:
            return 0
        ans = 0
        while stack:
            node, depth = stack.pop()
            if node:
                ans = max(ans, depth)
                if node.left:
                    stack.append((node.left, depth  + 1))
                if node.right:
                    stack.append((node.right, depth + 1))
        return ans
        #Time Complexity for this iterative solution is also O(n) as it visits every node
        #Space Complexity: Different than recursive as if the tree was like a linked list, we would continuously pop whatever we were appending, but if it was balance it would still be log n as the depth is log n