from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.l = []

        def r(node):
            if not node: return

            r(node.right)
            self.l.append(node.val)
            r(node.left)
        return r(root)
                

    def next(self) -> int:

        v = self.l.pop()
        return v


    def hasNext(self) -> bool:
        if self.l:
            return True
        return False
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()

r = TreeNode(7)
r.left = TreeNode(3)
r.right = TreeNode(15)
r.right.left = TreeNode(9)
r.right.right = TreeNode(20)

o = BSTIterator(r)
print(o.next())
