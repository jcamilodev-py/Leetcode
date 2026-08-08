from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        l = []
        ans = float('inf')
        def r(node):
            if not node:
                return

            l.append(node.val)
            r(node.left)
            r(node.right)


        r(root)

        l.sort()
        i, j = 0, len(l)-1

        while i < j:
            ans = min(ans, l[i+1] - l[i], l[j] - l[j-1])
            i+=1
            j-=1

        return ans



r = TreeNode(96)
r.left = TreeNode(12)
r.left.right = TreeNode(13)
r.left.right.right = TreeNode(52)
r.left.right.right.left = TreeNode(29)

s = Solution()
print(s.minDiffInBST(r))