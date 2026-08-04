from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def preorder(node):
            if not node:
                return

            node.left, node.right = node.right, node.left
            preorder(node.left)
            preorder(node.right)

        preorder(root)

        return root




r = TreeNode(4)
r.left = TreeNode(2)
r.right = TreeNode(7)
r.left.left = TreeNode(1)
r.left.right = TreeNode(3)
r.right.right = TreeNode(9)
r.right.left = TreeNode(6)

s = Solution()
print(s.invertTree(r))