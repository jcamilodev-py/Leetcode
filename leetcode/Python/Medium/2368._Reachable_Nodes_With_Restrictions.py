class Solution:
    def reachableNodes(self, n: int, edges: list[list[int]], restricted: list[int]) -> int:
        parent = list(range(n))

        rank = [0] * n

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
                rank[ra]+=1
            return True

        seen = set(restricted)

        for u, v in edges:
            if u not in seen and v not in seen:
                union(u, v)
        root = find(0)

        return sum(find(i) == root for i in range(n))

            
            
s = Solution()
print(s.reachableNodes(n = 4, edges = [[2,1],[0,1],[0,3]], restricted = [3,2]))