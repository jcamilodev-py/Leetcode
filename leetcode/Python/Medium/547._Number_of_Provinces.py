from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        ans = len(isConnected)
        n = len(isConnected)
        used = set()

        def dfs(i):
            nonlocal ans

            used.add(i)

            for j in range(n):
                if isConnected[i][j] == 1 and i != j and j not in used:
                    ans-=1
                    dfs(j)


        for x in range(n):
            dfs(x)

        return ans





s = Solution()
print(s.findCircleNum(isConnected = [[1,1,1],[1,1,1],[1,1,1]]))