# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        l = []
        def r(node):
            if not node:
                return

            if node.val == target.val:
                l.append(node)

            r(node.left)
            r(node.right)
            
        r(cloned)

        return l[0]



r = TreeNode(7)
r.left = TreeNode(4)
r.right = TreeNode(3)
r.right.left = TreeNode(6)
r.right.right = TreeNode(19)

s =  Solution()
print(s.getTargetCopy(r, r, TreeNode(3)))