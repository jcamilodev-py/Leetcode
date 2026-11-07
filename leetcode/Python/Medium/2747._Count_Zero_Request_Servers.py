from collections import defaultdict
from typing import List


class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        logs.sort(key=lambda x: x[1])
        queries = [[i, q] for i, q in enumerate(queries)]

        queries.sort(key=lambda x: x[1])
        ans = [0] * len(queries)

        dic = defaultdict(int)
        l, r = 0, 0

        for i, j in queries:
            while r < len(logs) and logs[r][1] <= j:
                v = logs[r][0]
                dic[v]+=1
                r+=1

            while l < r and logs[l][1] < j - x:
                v = logs[l][0]
                dic[v]-=1

                if dic[v] == 0:
                    del dic[v]

                l+=1

            ans[i] = n - len(dic)

        return ans






s = Solution()
print(s.countServers(n = 3, logs = [[1,3],[2,6],[1,5]], x = 5, queries = [10,11]))