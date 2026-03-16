from typing import List

class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        ans = 0
        for i in range(len(hours)):

            for j in range(i+1, len(hours)):

                if (hours[i] + hours[j]) % 24 == 0:
                    ans +=1
        return ans

s = Solution()
print(s.countCompleteDayPairs([72,48,24,3]))