from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        seen = set()
        ans = [False]

        def r(node):
            if not node:
                return

            if node.val in seen:
                ans[0] = True

            seen.add(k - node.val)
            r(node.left)
            r(node.right)

        r(root)

        return ans[0]
                

r = TreeNode(5)
r.left = TreeNode(3)
r.left.left = TreeNode(2)
r.left.right = TreeNode(4)
r.right = TreeNode(6)
r.right.right = TreeNode(7)

s = Solution()
print(s.findTarget(r, 9))