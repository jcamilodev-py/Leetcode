from typing import List


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []

        def recorrer(nodo):
            if not nodo:
                return
            
            recorrer(nodo.left)
            output.append(nodo.val)
            recorrer(nodo.right)
        
        recorrer(root)
        return output