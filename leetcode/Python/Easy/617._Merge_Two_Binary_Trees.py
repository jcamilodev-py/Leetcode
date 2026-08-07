from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:

        def r(node1, node2):

            if node1 and node2:
                ans = TreeNode(node1.val + node2.val)
            elif node1 and not node2:
                ans = TreeNode(node1.val)
            elif not node1 and node2:
                ans = TreeNode(node2.val)
            else:
                return
            
            ans.left = r(node1.left if node1 else None, node2.left if node2 else None)
            ans.right = r(node1.right if node1 else None, node2.right if node2 else None)

            return ans

        return r(root1, root2)


r1 = TreeNode(1)
r1.left = TreeNode(3)
r1.right = TreeNode(2)
r1.left.left = TreeNode(5)

r2 = TreeNode(2)
r2.left = TreeNode(1)
r2.right = TreeNode(3)
r2.left.right = TreeNode(4)
r2.right.right = TreeNode(7)


s = Solution()
print(s.mergeTrees(r1, r2))