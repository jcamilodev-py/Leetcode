# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sufficientSubset(self, root: TreeNode | None, limit: int) -> TreeNode | None:

        def dfs(node, current_sum):

            if not node:
                return False
            
            current_sum+=node.val
            if not node.left and not node.right:
                return current_sum >= limit

            l = dfs(node.left, current_sum)
            r = dfs(node.right, current_sum)

            if not l:
                node.left = None

            if not r:
                node.right = None

            return l or r

        return root if dfs(root, 0) else None





r = TreeNode(1)
r.left = TreeNode(2)
r.left.left = TreeNode(-5)

r.right = TreeNode(-3)
r.right.left = TreeNode(4)

s = Solution()
print(s.sufficientSubset(r, -1))