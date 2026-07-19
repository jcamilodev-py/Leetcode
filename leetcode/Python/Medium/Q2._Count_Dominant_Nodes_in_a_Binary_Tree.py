# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countDominantNodes(self, root: TreeNode | None) -> int:
        ans = 0
        def dfs(node):
            nonlocal ans
            if not node:
                return 0
            
                        
            l = dfs(node.left)
            r = dfs(node.right)
            sub = max(node.val, l, r)

            if sub == node.val:
                ans+=1

            return sub
        dfs(root)

        return ans




r = TreeNode(5)
r.left = TreeNode(3)
r.left.left = TreeNode(2)
r.left.right = TreeNode(4)
r.right = TreeNode(8)
r.right.right = TreeNode(1)
r.right.left = TreeNode(7)

s = Solution()
print(s.countDominantNodes(r))