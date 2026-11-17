class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: list[list[int]]) -> list[int]:

        indegree = {i:0 for i in range(n)}

        for u, v in edges:
            indegree[v]+=1

        return [i for i in indegree if indegree[i] == 0]


s = Solution()
print(s.findSmallestSetOfVertices(n = 6, edges = [[0,1],[0,2],[2,5],[3,4],[4,2]]))