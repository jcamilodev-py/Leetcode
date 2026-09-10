# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        ans = [0]
        
        def dfs(node):
            if not node:
                return (0, 0)

            sl, cl = dfs(node.left)
            sr, cr = dfs(node.right)

            ts = node.val + sl + sr
            ct = 1 + cl + cr

            average = ts // ct

            if average == node.val:
                ans[0]+=1


            return (ts, ct)
                
        dfs(root)

        return ans[0]




r = TreeNode(4)
r.left = TreeNode(8)
r.left.left = TreeNode(0)
r.left.right = TreeNode(1)
r.right = TreeNode(5)
r.right.right = TreeNode(6)

s = Solution()
print(s.averageOfSubtree(r))