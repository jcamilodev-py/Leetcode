# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def dfs(node, p, q):
            if node in {None, p, q}:
                return node
            
            l = dfs(node.left, p, q)
            r = dfs(node.right, p, q)

            if l and r:
                return node
            
            return l or r
        
        return dfs(root, p, q)
            


r = TreeNode(3)
r.left = TreeNode(5)
r.left.left = TreeNode(6)
r.left.right = TreeNode(2)
r.left.right.left = TreeNode(7)
r.left.right.right = TreeNode(4)
r.right = TreeNode(1)
r.right.right = TreeNode(8)
r.right.left = TreeNode(0)

s = Solution()
print(s.lowestCommonAncestor(r, TreeNode(5), TreeNode(1)))