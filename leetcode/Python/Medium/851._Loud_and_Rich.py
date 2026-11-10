from collections import defaultdict


class Solution:
    def loudAndRich(self, richer: list[list[int]], quiet: list[int]) -> list[int]:
        n = len(quiet)

        dic = defaultdict(set)

        visited = [0] * n

        for i,j in richer:
            dic[j].add(i)
            dic[j].add(j)
        

        def dfs(node):
            if visited[node]:
                return dic[node]

            visited[node] = True

            for i in list(dic[node]):
                dic[node].update(dfs(i))

            return dic[node]

        for i in range(n):
            dfs(i)

        ans = [0] * n

        for i in dic:
            m = [float('inf'), i]
            for j in dic[i]:
                if quiet[j] < m[0]:
                    m[0] = quiet[j]
                    m[1] = j

            ans[i] = m[1]

        return ans
                
        




s = Solution()
print(s.loudAndRich([[1,0],[2,1],[3,1],[3,7],[4,3],[5,3],[6,3]], quiet = [3,2,5,4,6,1,7,0]))