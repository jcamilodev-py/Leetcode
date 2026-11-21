from collections import defaultdict
from functools import cache


class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        adj = defaultdict(list)
        for i in range(1, n):
            adj[parent[i]].append(i)

        last = [-1] * 26

        def dfs(node):
            current = ord(s[node]) - ord('a')
            prev = last[current]
            if prev != -1:parent[node] = prev
            last[current] = node
            for i in adj[node]:dfs(i)
            last[current] = prev

        dfs(0)

        adj2 = defaultdict(list)
        for i in range(1, n):adj2[parent[i]].append(i)

        @cache
        def dfs2(node):
            total = 1
            for i in adj2[node]:total+=dfs2(i)
            return total

        ans = []
        for i in range(n):ans.append(dfs2(i))
        return ans