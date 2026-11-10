from collections import deque
from typing import List


class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]

        degree = [0] * n

        for i, j in relations:
            adj[i-1].append(j-1)
            degree[j-1]+=1

        d = deque(i for i, j in enumerate(degree) if j == 0)

        ans = 0
        count = 0

        while d:
            ans+=1
            for _ in range(len(d)):
                course = d.popleft()
                count+=1
                for i in adj[course]:
                    degree[i]-=1

                    if degree[i] == 0:
                        d.append(i)

        return ans if count == n else -1



            

s = Solution()
print(s.minimumSemesters(3, [[1,3],[2,3]]))