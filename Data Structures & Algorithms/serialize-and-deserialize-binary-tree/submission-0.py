# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        #preorder
        preor = []
        def preorder(node):
            if not node:
                preor.append("N")
                return None
            preor.append(str(node.val))
            preorder(node.left)
            preorder(node.right)
        preorder(root)
        ans = ",".join(preor)
        return ans
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(",")
        i = 0
        def create():
            nonlocal i
            if vals[i] == "N":
                i += 1
                return None
            root = TreeNode(vals[i])
            i += 1
            root.left = create()
            root.right = create()
            return root
        return create()


        
