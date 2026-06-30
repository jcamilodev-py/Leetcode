from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def dfs(node, remaining):
            if not node:
                return
            if not node.left and not node.right:
                if remaining - node.val == 0:
                    return True
            else:
                return dfs(node.left, remaining-node.val) or dfs(node.right, remaining-node.val)
        
        return True if dfs(root, targetSum) else False
        


root1 = TreeNode(5)
root1.left = TreeNode(4)
root1.left.left = TreeNode(11)
root1.left.left.left = TreeNode(7)
root1.left.left.right = TreeNode(2)
root1.right = TreeNode(8)
root1.right.left = TreeNode(13)
root1.right.right = TreeNode(4)
root1.right.right.right = TreeNode(1)


s = Solution()
print(s.hasPathSum(root1, 22))

