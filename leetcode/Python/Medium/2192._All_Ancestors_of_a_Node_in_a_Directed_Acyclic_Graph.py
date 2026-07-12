from typing import List
from collections import defaultdict, deque

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = [[] for _ in range(n)]
        ans = defaultdict(set)
        in_degree = [0] * n

        def bfs():
            while queue:
                u = queue.popleft()

                for v in graph[u]:
                    ans[v].add(u)
                    ans[v].update(ans[u])

                    in_degree[v]-=1
                    if in_degree[v] == 0:
                        queue.append(v)


        for fromm, to in edges:
            graph[fromm].append(to)
            in_degree[to]+=1
        
        queue = deque([i for i in range(n) if in_degree[i] == 0])
        
        

        bfs()
        
        return [sorted(ans[i]) for i in range(n)]



s = Solution()
print(s.getAncestors(8, [[0,3],[0,4],[1,3],[2,4],[2,7],[3,5],[3,6],[3,7],[4,6]]))