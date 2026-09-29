from collections import defaultdict


class Solution:
    def minReorder(self, n: int, connections: list[list[int]]) -> int:
        ans = 0

        edges = { (i,j) for i,j in connections}


        dic = defaultdict(list)

        v = set()

        for i, j in connections:
            dic[i].append(j)
            dic[j].append(i)

        def dfs(c):
            nonlocal edges, dic, v, ans

            for i in dic[c]:
                if i in v:
                    continue

                if (i, c) not in edges:
                    ans+=1

                v.add(i)
                dfs(i)

        v.add(0)
        dfs(0)
        return ans

            


s = Solution()
print(s.minReorder(n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]))