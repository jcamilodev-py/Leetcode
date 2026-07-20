from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        while root != None:
            if root.val > val:
                root = root.left
            elif root.val < val:
                root = root.right
            elif root.val == val:
                return root
            
             


r = TreeNode(4)
r.left = TreeNode(2)
r.left.left = TreeNode(1)
r.left.right = TreeNode(3)
r.right = TreeNode(7)

s = Solution()
print(s.searchBST(r, 5))