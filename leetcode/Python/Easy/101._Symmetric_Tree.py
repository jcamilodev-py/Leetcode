from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def dfs_l(node, l):
            if not node:
                l.append(None)
                return
            
            l.append(node.val)
            dfs_l(node.left, l)
            dfs_l(node.right, l)
        
        def dfs_r(node, l):
            if not node:
                l.append(None)
                return
            
            l.append(node.val)
            dfs_r(node.right, l)
            dfs_r(node.left, l)
        
        l = []
        l2 = []
        dfs_l(root.left, l)
        dfs_r(root.right, l2)

        return l == l2




r = TreeNode(1)
r.left = TreeNode(2)
r.left.left = TreeNode(3)
r.left.right = TreeNode(4)
r.right = TreeNode(2)
r.right.left = TreeNode(4)
r.right.right = TreeNode(3)

s = Solution()
print(s.isSymmetric(r))