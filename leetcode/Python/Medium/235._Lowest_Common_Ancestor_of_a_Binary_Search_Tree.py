# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def dfs(node, p, q):
            if not node:
                return
            if node == p or node == q:
                return node

            l = dfs(node.left, p, q)
            r = dfs(node.right, p, q)

            if l and r:
                return node

            return l if l else r
        
        return dfs(root, p, q)
            
r = TreeNode(6)
r.left = TreeNode(2)
r.left.left = TreeNode(0)
r.left.right = TreeNode(4)
r.left.right.left = TreeNode(3)
r.left.right.right = TreeNode(5)

r.right = TreeNode(8)
r.right.left = TreeNode(7)
r.right.right = TreeNode(9)

# p and q are TreeNodes
s = Solution()
print(s.lowestCommonAncestor(r, 2, 8))