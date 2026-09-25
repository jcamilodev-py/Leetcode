from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        tree = []
        def preorder(node):
            if not node:
                return

            tree.append(str(node.val))
            preorder(node.left)
            preorder(node.right)

        preorder(root)
        return ",".join(tree)
        

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """

        if not data:
            return

        vals = list(map(int, data.split(",")))
        self.i = 0

        def build(l, u):
            if self.i == len(vals):
                return 

            val = vals[self.i]

            if val < l or val > u:
                return

            self.i+=1
            node = TreeNode(val)
            node.left = build(l, val)
            node.right = build(val, u)

            return node

        return build(float("-inf"), float("inf"))
        

        

    
r = TreeNode(2)
r.left = TreeNode(1)
r.right = TreeNode(3)

c1 = Codec()
print(c1.serialize(r))
print(c1.deserialize(c1.serialize(r)))

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans