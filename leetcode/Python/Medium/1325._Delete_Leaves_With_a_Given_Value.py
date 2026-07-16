from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        
        def dfs(node, target):
            if not node:
                return None
            
            node.left = dfs(node.left, target)
            node.right = dfs(node.right, target)

            if node.left is None and node.right is None and node.val == target:
                return None
            return node
        
        return dfs(root, target)


r = TreeNode(1)
r.left = TreeNode(2)
r.left.left = TreeNode(2)
r.right = TreeNode(3)
r.right.left = TreeNode(2)
r.right.right = TreeNode(4)

s = Solution()
print(s.removeLeafNodes(r, 2))