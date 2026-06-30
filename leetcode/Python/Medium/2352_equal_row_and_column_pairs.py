from typing import List
from collections import defaultdict

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        ans = 0
        dic = defaultdict(int)

        for i in grid:
            dic[tuple(i)]+=1
        columnas = list(zip(*grid))

        for col in columnas:
            if tuple(col) in dic:
                ans+=1*dic[tuple(col)]

        return ans


s = Solution()
print(s.equalPairs([[3,2,1],[1,7,6],[2,7,7]]))