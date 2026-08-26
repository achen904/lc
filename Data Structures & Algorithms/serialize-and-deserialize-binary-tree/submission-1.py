# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        #we can deserialize a binary tree if we know both its preorder
        preorder = []
        def dfspreorder(node):
            nonlocal preorder
            if not node:
                preorder.append("N")
                return
            preorder.append(str(node.val))
            dfspreorder(node.left)
            dfspreorder(node.right)
        dfspreorder(root)
        return ",".join(preorder)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        split = data.split(",")
        preInd = 0
        def dfs():
            nonlocal preInd
            if split[preInd] == "N":
                preInd += 1
                return None
            node = TreeNode(split[preInd])
            preInd += 1
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()
