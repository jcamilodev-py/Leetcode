from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def insertIntoMaxTree(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return 
        arr = []
        def cartesian(arr):
            stack = []
            root = None
        
            for i in arr:
                current = TreeNode(i)
                last = None
        
                while stack and stack[-1].val < i:
                    last = stack.pop()
        
                if stack:
                    stack[-1].right = current
                else:
                    root = current
        
                current.left = last
                stack.append(current)
            return root
        
        def inorder(node):
            if not node:
                return
            
            inorder(node.left)
            arr.append(node.val)
            inorder(node.right)

        inorder(root)
        arr.append(val)
        return cartesian(arr)


r = TreeNode(5)
r.left = TreeNode(2)
r.right = TreeNode(4)
r.left.right = TreeNode(1)

s = Solution()
print(s.insertIntoMaxTree(r, 3))