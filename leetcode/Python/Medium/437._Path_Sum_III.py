from typing import Optional
from collections import defaultdict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        dic = defaultdict(int)
        dic[0] = 1

        def dfs(node, current_sum):
            if not node:
                return 0
            
            current_sum+= node.val
            c = current_sum - targetSum
            r = dic.get(c, 0) 
            dic[current_sum]+=1
            v = r + dfs(node.left, current_sum) + dfs(node.right, current_sum)
            dic[current_sum]-=1

            return v

        return dfs(root, 0)


r = TreeNode(10)
r.left = TreeNode(5)
r.left.left = TreeNode(3)
r.left.left.left = TreeNode(3)
r.left.left.right = TreeNode(-2)
r.left.right = TreeNode(2)
r.left.right.right = TreeNode(1)
r.right = TreeNode(-3)
r.right.right = TreeNode(11)



s = Solution()
print(s.pathSum(r, 8))