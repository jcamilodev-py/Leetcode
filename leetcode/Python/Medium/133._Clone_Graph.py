# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node

        dic = {}

        def dfs(node):
            if node in dic:
                return dic[node]

            v = Node(node.val)
            dic[node] = v

            for n in node.neighbors:
                dfs(v.neighbors.append(dfs(n)))

            return v

        return dfs(node)