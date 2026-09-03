from typing import Optional
from collections import deque

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':

        def bfs():
            d = deque([root])

            while d:

                n = len(d)
                prev = None
                for _ in range(n):
                    node = d.popleft()

                    if prev:
                        prev.next = node

                    prev = node
                    if node:
                        if node.left:
                            d.append(node.left)
                        if node.right:
                            d.append(node.right)

            return root

        return bfs()