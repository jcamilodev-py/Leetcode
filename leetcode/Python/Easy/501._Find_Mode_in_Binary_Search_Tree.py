from typing import List, Optional
from collections import defaultdict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        dic = defaultdict(int)
        ans = []

        def preorder(node):
            if not node:
                return
            
            dic[node.val]+=1

            preorder(node.left)
            preorder(node.right)

        preorder(root)

        m = max(dic.values())

        for i in dic:
            if dic[i] == m:
                ans.append(i)

        return ans



r = TreeNode(1)
r.right = TreeNode(2)

s = Solution()
print(s.findMode(r))