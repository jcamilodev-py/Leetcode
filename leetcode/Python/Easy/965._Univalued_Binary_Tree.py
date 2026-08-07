from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
       def r(node, ans):
           if not node:
               return 

           ans.append(node.val)

           r(node.left, ans)
           r(node.right, ans)

           return ans

       t = r(root, []) 

       return True if t.count(t[0]) == len(t) else False




r = TreeNode(1)
r.left = TreeNode(1)
r.left.left = TreeNode(1)
r.left.right = TreeNode(1)
r.right = TreeNode(1)
r.right.right = TreeNode(1)

s = Solution()
print(s.isUnivalTree(r))