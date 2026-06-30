from typing import List

class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 1:
            return 1
        ans = 1
        r = 1
        for i in range(1, n):
            if prices[i] +1 == prices[i-1]:
                r+=1
                ans+=r
            else:
                r = 1
                ans+=1
        return ans



s = Solution()
print(s.getDescentPeriods([1]))