class Solution:
    def eventualSafeNodes(self, graph: list[list[int]]) -> list[int]:
        n = len(graph)
        dic = {}
        ans = []

        def dfs(i):
            if i in dic:
                return dic[i]
            dic[i] = False

            for j in graph[i]:
                if not dfs(j):
                    return False

            dic[i] = True
            return True

        for i in range(n):
            if dfs(i):
                ans.append(i)

        return ans



s = Solution()
print(s.eventualSafeNodes(graph = [[1,2],[2,3],[5],[0],[5],[],[]]))