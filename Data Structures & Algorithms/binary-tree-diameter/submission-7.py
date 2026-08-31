# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #iterative solution
        stack = []
        ans = 0
        map = defaultdict(int) #node: height
        if not root:
            return 0
        stack.append(root)
        while stack:
            #want to get to bottom so we append to stack before popping
            node = stack[-1]
            #check if child are already in map or else infinite loop
            if node.left and node.left not in map:
                stack.append(node.left)
            elif node.right and node.right not in map:
                stack.append(node.right)
            else:
                node = stack.pop()
                map[node] = (1 + max(map[node.left], map[node.right]))
                ans = max(ans,map[node.left] + map[node.right])
        return ans

            