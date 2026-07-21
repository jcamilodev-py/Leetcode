from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        
        ans = 0
        def dfs(node):
            nonlocal ans
            
            if not node:
                return 0
            
            l = dfs(node.left)
            r = dfs(node.right)

            ans+= abs(l - r)
            
            
            return l + r + node.val

        dfs(root)
        return ans


r = TreeNode(4)
r.left = TreeNode(2)
r.left.left = TreeNode(3)
r.left.right = TreeNode(5)
r.right = TreeNode(9)
r.right.right = TreeNode(7)

s = Solution()
print(s.findTilt(r))