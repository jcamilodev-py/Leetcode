from collections import defaultdict, deque


class Solution:
    def isPrintable(self, targetGrid: list[list[int]]) -> bool:

        def h(target_grid):
            n, m = len(target_grid), len(target_grid[0])
            inf = float('inf')

            dic = {}

            for i in range(n):
                for j in range(m):
                    k = target_grid[i][j]

                    if k not in dic:
                        dic[k] = [inf, -inf, inf, -inf]

                    b = dic[k]
                    b[0] = min(b[0], i)
                    b[1] = max(b[1], i)
                    b[2] = min(b[2], j)
                    b[3] = max(b[3], j)

            return dic

        dic = h(targetGrid)
        adj = defaultdict(set)

        for k in dic:
            for i in range(dic[k][0], dic[k][1]+1):
                for j in range(dic[k][2], dic[k][3]+1):
                    if targetGrid[i][j] == k:
                        continue

                    adj[k].add(targetGrid[i][j])

                
        indegree = {i:0 for i in dic}

        for k in adj:
            for v in adj[k]:
                indegree[v]+=1

        d = deque(i for i in indegree if indegree[i] == 0)
        count = 0
        while d:
            i = d.popleft()
            count+=1

            for j in adj[i]:
                indegree[j]-=1
                if indegree[j] == 0:
                    d.append(j)

        return count == len(indegree)

                        



                               

s = Solution()
print(s.isPrintable([[1,1,1,1],[1,1,3,3],[1,1,3,4],[5,5,1,4]]))