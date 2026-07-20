from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        def bst(node, key):
            if not node:
                return None
            
            if key < node.val:
                node.left = bst(node.left, key)
            elif key > node.val:
                node.right = bst(node.right, key)

            else:

                if not node.left:
                    return node.right
                
                if not node.right:
                    return node.left
                

                s = node.right
                while s.left:
                    s = s.left
                
                node.val = s.val
                node.right = bst(node.right, s.val)

            return node
        return bst(root, key)


        

r = TreeNode(5)
r.left = TreeNode(3)
r.left.left = TreeNode(2)
r.left.right = TreeNode(4)
r.right = TreeNode(6)
r.right.right = TreeNode(7)

s = Solution()
print(s.deleteNode(r, 3))