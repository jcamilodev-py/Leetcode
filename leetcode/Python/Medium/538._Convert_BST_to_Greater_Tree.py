from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return root
        current = [0]
        def dfs(node):
            if not node:
                return

            dfs(node.right)
            node.val+=current[0]
            current[0] = node.val
            dfs(node.left)


        dfs(root)

        return root.val




r = TreeNode(4)
r.left = TreeNode(1)
r.left.left = TreeNode(0)
r.left.right = TreeNode(2)
r.left.right.right = TreeNode(3)

r.right = TreeNode(6)
r.right.left = TreeNode(5)
r.right.right = TreeNode(7)
r.right.right.right = TreeNode(8)

s = Solution()
print(s.convertBST(r))