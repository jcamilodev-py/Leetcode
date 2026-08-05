from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        ans = []

        def preorder(node):
            if not node:
                return

            if node.left:
                ans.append(min(node.left.val, node.right.val))
            else:
                ans.append(node.val)             

            preorder(node.left)
            preorder(node.right)

        preorder(root)

        ans.sort()

        for i in range(1, len(ans)):
            if ans[i] != ans[0]:
                return ans[i]

        return -1



r = TreeNode(2)
r.left = TreeNode(2)
r.right = TreeNode(5)
r.right.left = TreeNode(5)
r.right.right = TreeNode(7)

s = Solution()
print(s.findSecondMinimumValue(r))