from typing import List


class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        m = len(mat)
        dp = [set() for _ in range(m+1)]
        dp[0].add(0)

        for i in range(m):
            for s in dp[i]:
                for j in mat[i]:
                    dp[i+1].add(s + j)

        return min(abs(target-i) for i in dp[m])




s = Solution()
print(s.minimizeTheDifference(mat = [[1,2,3],[4,5,6],[7,8,9]], target = 13))