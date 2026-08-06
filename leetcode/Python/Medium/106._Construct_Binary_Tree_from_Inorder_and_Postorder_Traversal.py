from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        dic = {j:i for i,j in enumerate(inorder)}

        def h(l, r):
            if l > r:
                return

            root = TreeNode(postorder.pop())

            idx = dic[root.val]

            root.right = h(idx + 1, r)
            root.left = h(l, idx - 1)

            return root
        
        return h(0, len(inorder) - 1)


s = Solution()
print(s.buildTree(inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]))