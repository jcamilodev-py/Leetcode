from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        l = []
        l2 = []
        def preorder(node, l):
            if not node:
                return l.append(None)

            l.append(node.val)
            preorder(node.left, l)
            preorder(node.right, l)

        preorder(p, l)
        preorder(q, l2)

        return l == l2


r1 = TreeNode(1)
r1.left = TreeNode(2)
r1.right = TreeNode(3)

r2 = TreeNode(1)
r2.left = TreeNode(2)
r2.right = TreeNode(3)

s = Solution()
print(s.isSameTree(r1, r2))