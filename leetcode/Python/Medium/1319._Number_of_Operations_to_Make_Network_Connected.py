class Solution:
    def makeConnected(self, n: int, connections: list[list[int]]) -> int:
        if len(connections) < n-1:
            return -1
        count = n-1
        
        parent = list(range(n))
        ans = 0

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

        for u, v in connections:
            if not union(u, v):
                ans+=1
            else:
                count-=1

        if count <= ans:
            return min(count, ans)
        return -1



s = Solution()
print(s.makeConnected(n = 4, connections = [[0,1],[0,2],[1,2]]))