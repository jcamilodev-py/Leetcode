# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def postorderTraversal(self, root):
        resultado = []
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        def recorrer(nodo):
            if not nodo:
                return
            
            recorrer(nodo.left)
            recorrer(nodo.right)
            resultado.append(nodo.val)

        recorrer(root)
        return resultado

        