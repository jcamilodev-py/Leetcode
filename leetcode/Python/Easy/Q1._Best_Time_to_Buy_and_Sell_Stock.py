from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = float("inf")
        ans = 0

        for i in prices:
            if i < best:
                best = i
            
            if i - best > ans:
                ans = i - best
        
        return ans

        


s = Solution()
print(s.maxProfit([7,6,4,3,1]))