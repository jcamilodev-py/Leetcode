from typing import List, Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []

        ans = []
        d = deque([root])

        while d:
            tam = len(d)

            for i in range(tam):
                v = d.popleft()
                if v.left:
                    d.append(v.left)
                if v.right:
                    d.append(v.right)
                
                if i+1 == tam:
                    ans.append(v.val)
        return ans
                    


r = TreeNode(1)
r.left = TreeNode(2)
r.left.right = TreeNode(5)
r.right = TreeNode(3)
r.right.right = TreeNode(4)

s = Solution()
print(s.rightSideView(r))