from typing import List
from collections import defaultdict, deque

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = defaultdict(list)

        for i, j in enumerate(equations):
            a, b = j
            adj[a].append([b, values[i]])
            adj[b].append([a, 1 / values[i]])

        def bfs(src, target):

            if src not in adj or target not in adj:
                return -1

            d, visit = deque(), set()

            d.append([src, 1])
            visit.add(src)

            while d:
                print(d)
                n, w = d.popleft()
                if n == target:
                    return w

                for i, j in adj[n]:
                    if i not in visit:
                        d.append([i, w * j])
                        visit.add(i)

            return -1


        return [bfs(i[0], i[1]) for i in queries]



s = Solution()
print(s.calcEquation(equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]))