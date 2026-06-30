from typing import Optional
# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def recursion(root, low, high):
            if not root:
                return 0
            if root.val < low:
                return recursion(root.right, low, high)
            elif root.val > high:
                return recursion(root.left, low, high)
            else:
                return root.val + recursion(root.left, low, high) + recursion(root.right, low, high)  
                          

        return recursion(root, low, high)


root1 = TreeNode(10)
root1.left = TreeNode(5)
root1.right = TreeNode(15)
root1.left.left = TreeNode(3)
root1.left.right = TreeNode(7)
root1.right.right = TreeNode(18)

s = Solution()
print(s.rangeSumBST(root1, 7, 15))