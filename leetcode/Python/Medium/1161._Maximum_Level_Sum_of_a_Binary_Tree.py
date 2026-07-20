from typing import Optional
from collections import deque, defaultdict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        d = deque([root])
        ans = [float("-inf"), 0]

        i = 1
        while d:
            lenn = len(d)
            current = []

            for _ in range(lenn):
                node = d.popleft()
                current.append(node.val)

                if node.left:
                    d.append(node.left)
                
                if node.right:
                    d.append(node.right)

            s = sum(current)
            if ans[0] < s:
                ans[0], ans[1] = s, i
            
            i+=1
        
        return ans[1]
        


r = TreeNode(1)
r.left = TreeNode(7)
r.left.left = TreeNode(7)
r.left.right = TreeNode(-8)
r.right = TreeNode(0)

s = Solution()
print(s.maxLevelSum(r))