class Solution:
    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
        ans = []
        n = len(graph)

        def dfs(i, current):
            current.append(i)

            if i == n-1:
                ans.append(current.copy())
                current.pop()
                return

            for j in graph[i]:
                dfs(j, current)

            current.pop()

        dfs(0, [])

        return ans


s = Solution()
print(s.allPathsSourceTarget([[1,2],[3],[3],[]]))