from typing import List

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        n = len(tickets)
        total = 0
        for i in range(n):
            if i < k:
                s = min(tickets[i], tickets[k])
                total += s
            elif i > k:
                s = min(tickets[k]-1, tickets[i])
                total += s

        return total + tickets[k]



s = Solution()
print(s.timeRequiredToBuy([2,3,2], k = 2))