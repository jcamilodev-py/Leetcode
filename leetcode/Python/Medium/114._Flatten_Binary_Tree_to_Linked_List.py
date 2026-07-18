from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root or not root.left and not root.right:
            return root
        l = []
        
        def preorder(node):
            if not node:
                return
            
            l.append(node)

            preorder(node.left)
            preorder(node.right)

        preorder(root)

    
        current = root
        for i in l:
            current.left = None
            current.right = i

            current = current.right
        
        return root
            


r = TreeNode(1)


s = Solution()
print(s.flatten(r))