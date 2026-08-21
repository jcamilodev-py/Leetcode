from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        ans = []
        def dfs(node, l):
            if not node:
                return

            if not node.left and not node.right:
                l.append(str(node.val))
                ans.append("->".join(l))
                l.pop()
                return

            l.append(str(node.val))
            dfs(node.left, l)
            dfs(node.right, l)
            l.pop()

        dfs(root, [])
        return ans 
                 


r = TreeNode(1)
r.right = TreeNode(4)
r.right.left = TreeNode(3)
r.right.left.left = TreeNode(2)
r.right.right = TreeNode(5)
r.right.right = TreeNode(6)



s = Solution()
print(s.binaryTreePaths(r))
