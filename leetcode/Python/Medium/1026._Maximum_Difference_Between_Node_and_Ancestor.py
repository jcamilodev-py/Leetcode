from typing import Optional

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs(node, maxNode, minNode):
            if not node:
                return abs(maxNode - minNode)
            
            return max (dfs(node.left, max(maxNode, node.val), min(minNode, node.val)),
            dfs(node.right, max(maxNode, node.val), min(minNode, node.val)))
        
        return dfs(root, float("-inf"), float("inf"))



t = TreeNode(8)
t.left = TreeNode(3)
t.left.left = TreeNode(1)
t.left.right = TreeNode(6)
t.left.right.left = TreeNode(4)
t.left.right.right = TreeNode(7)
t.right = TreeNode(10)
t.right.right = TreeNode(14)
t.right.right.right = TreeNode(13)

s = Solution()
print(s.maxAncestorDiff(t))