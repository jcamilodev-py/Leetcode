from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        l1 = []
        l2 = []

        def dfs(root, l):
            if not root:
                return
            if not root.left and not root.right:
                l.append(root.val)
            

            dfs(root.left, l)
            dfs(root.right, l)
        
        dfs(root1, l1)
        dfs(root2, l2)
        

        return l1 == l2
  
    
r = TreeNode(1)
r.left = TreeNode(2)
r.right = TreeNode(3)

r2 = TreeNode(1)
r2.left = TreeNode(3)
r2.right = TreeNode(2)

s = Solution()
print(s.leafSimilar(r, r2))