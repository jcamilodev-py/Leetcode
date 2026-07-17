from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        ans = []
        def dfs(node, listt, current_sum):
            if not node:
                return
            
            listt.append(node.val)

            current_sum = current_sum + node.val
            dfs(node.left, listt, current_sum)
            dfs(node.right, listt, current_sum)

            if node.left is None and node.right is None:
                if current_sum == targetSum:
                    ans.append(listt[:])
            listt.pop()
            
        dfs(root, [], 0)

        return ans




r = TreeNode(5)
r.left = TreeNode(4)
r.left.left = TreeNode(11)
r.left.left.left = TreeNode(7)
r.left.left.right = TreeNode(2)
r.right = TreeNode(8)
r.right.left = TreeNode(13)
r.right.right = TreeNode(4)
r.right.right.left = TreeNode(5)
r.right.right.right = TreeNode(1)

s = Solution()
print(s.pathSum(r, 22))