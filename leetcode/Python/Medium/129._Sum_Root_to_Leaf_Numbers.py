from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans = [0]
        current_sum = [0]

        def dfs(node):
            if not node:
                return
            current_sum[0]*=10
            current_sum[0]+=node.val

            
            if not node.left and not node.right:
                ans[0]+=current_sum[0]
                current_sum[0]-=node.val
                current_sum[0]//=10
                return


            if node.left:
                dfs(node.left)


            if node.right:
                dfs(node.right)

            current_sum[0]-=node.val
            current_sum[0]//=10

        dfs(root)

        return ans[0]



r = TreeNode(4)
r.left = TreeNode(9)
r.right = TreeNode(0)
r.left.left = TreeNode(5)
r.left.right = TreeNode(1)

s = Solution()
print(s.sumNumbers(r))