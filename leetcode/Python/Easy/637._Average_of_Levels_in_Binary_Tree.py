from typing import List, Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        ans = []

        def bfs(root):
            d = deque([root])
            s = 0

            while d:
                size = len(d)
                for _ in range(size):
                    node = d.popleft()

                    s+=node.val

                    if node.left:
                        d.append(node.left)

                    if node.right:
                        d.append(node.right)

                ans.append(s / size)
                s = 0

                    
        bfs(root)
        return ans


r = TreeNode(3)
r.left = TreeNode(9)
r.right = TreeNode(20)
r.right.left = TreeNode(15)
r.right.right = TreeNode(7)

s = Solution()
print(s.averageOfLevels(r))
