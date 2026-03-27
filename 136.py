from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum = float('inf')
        profit = 0
        for i in prices:
            if i < minimum:
                minimum = i
            if i - minimum > profit:

                profit = i - minimum

        return profit

s = Solution()
print(s.maxProfit([1,2,3,4,5]))