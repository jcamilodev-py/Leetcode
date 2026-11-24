class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        n = len(edges)
        parent = list(range(n+1))
        rank = [0] * (n+1)

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a, b):
            ra, rb = find(a), find(b)
            if ra == rb:
                return False                  
            if rank[ra] < rank[rb]:
                ra, rb = rb, ra
            parent[rb] = ra                  
            if rank[ra] == rank[rb]:
                rank[ra] += 1
            return True

        for u, v in edges:
            if not union(u, v):
                return [u, v]



s = Solution()
print(s.findRedundantConnection(edges = [[1,2],[2,3],[1,3]]))