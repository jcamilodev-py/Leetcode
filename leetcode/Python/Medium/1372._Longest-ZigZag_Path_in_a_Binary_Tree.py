from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        
        ans = 0
        
        def dfs(node):
            nonlocal ans
            
            if not node:
                return (-1, -1)
            
            l_izq, r_izq = dfs(node.left)
            l_der, r_der = dfs(node.right)
            
            l = r_izq + 1 
            r = l_der + 1  
            
            ans = max(ans, l, r)
            
            return (l, r)
        
        dfs(root)
        return ans

    

r = TreeNode(1)
r.right = TreeNode(1)
r.right.right = TreeNode(1)
r.right.right.right = TreeNode(1)
r.right.left = TreeNode(1)
r.right.right.left = TreeNode(1)
r.right.right.left.right = TreeNode(1)
r.right.right.left.right.right = TreeNode(1)

s = Solution()
print(s.longestZigZag(r))