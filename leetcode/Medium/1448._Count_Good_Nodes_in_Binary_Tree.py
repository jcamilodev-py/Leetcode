# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def recursion(node, current_max):
            if not node:
                return 0
            if node.val < current_max:
                return recursion(node.left, current_max) + recursion(node.right, current_max)
            else:
                return 1 + recursion(node.left, node.val) + recursion(node.right, node.val)
            
        
        return recursion(root, float('-inf'))



root1 = TreeNode(3)
root1.left = TreeNode(1)
root1.right = TreeNode(4)
root1.left.left = TreeNode(3)
root1.right.left = TreeNode(1)
root1.right.right = TreeNode(5)


s = Solution()
print(s.goodNodes(root1))