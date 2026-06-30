# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import List


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []

        def recorrer(nodo):
            if not nodo:
                return
        
            output.append(nodo.val)
            recorrer(nodo.left)
            recorrer(nodo.right)
        
        recorrer(root)
        return output
        
        
        



