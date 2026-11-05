from collections import defaultdict, deque


class Solution:
    def findShortestCycle(self, n: int, edges: list[list[int]]) -> int:
        ans = float('inf')
        adj = defaultdict(list)

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def bfs(i):
            nonlocal ans
            dist = [-1] * n
            parent = [-1] * n

            dist[i] = 0

            d = deque([i])

            while d:
                u = d.popleft()
                for v in adj[u]:
                    if dist[v] == -1:
                        dist[v] = dist[u]+1
                        parent[v] = u
                        d.append(v)
                        
                        
                    elif parent[u] != v:
                        ans = min(ans, dist[u] + dist[v] + 1)

        for i in range(n):
            bfs(i)


        return ans if ans != float('inf') else -1



s = Solution()
print(s.findShortestCycle(n = 7, edges = [[0,1],[1,2],[2,0],[3,4],[4,5],[5,6],[6,3]]))