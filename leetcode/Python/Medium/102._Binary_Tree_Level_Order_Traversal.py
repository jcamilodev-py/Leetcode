from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:


        def level_order(root):
            if not root:
                return []
            ans = []
            d = deque([root])

            while d:
                level = []
                for _ in range(len(d)):
                    node = d.popleft()
                    level.append(node.val)
                    if node.left:
                        d.append(node.left)
                    if node.right:
                        d.append(node.right)

                ans.append(level)

            return ans

        return level_order(root)



        



r = TreeNode(3)
r.left = TreeNode(9)
r.right = TreeNode(20)
r.right.left = TreeNode(15)
r.right.right = TreeNode(7)

s = Solution()
print(s.levelOrder(r))