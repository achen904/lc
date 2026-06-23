# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        ans = []
        queue = deque()
        queue.append(root)
        while queue:
            first = True
            n = len(queue)
            for i in range(n):
                node = queue.popleft()
                if first:
                    ans.append(node.val)
                    first = False
                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)
        return ans