from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        if self.h(head, root):
            return True

        if not root: 
            return False

        return self.isSubPath(head, root.left) or self.isSubPath(head, root.right)

    def h(self, list_node, tree_node):
        if not list_node: 
            return True

        if not tree_node or list_node.val != tree_node.val:
            return False

        return self.h(list_node.next, tree_node.left) or self.h(list_node.next, tree_node.right)



l = ListNode(4)
l.next = ListNode(2)
l.next.next = ListNode(8)

r = TreeNode(1)
r.left = TreeNode(4)
r.left.right = TreeNode(2)
r.left.right.left = TreeNode(1)
r.right = TreeNode(4)
r.right.left = TreeNode(2)
r.right.left.left = TreeNode(6)
r.right.left.right = TreeNode(8)
r.right.left.right.left = TreeNode(1)
r.right.left.right.right = TreeNode(3)



s = Solution()
print(s.isSubPath(l, r))