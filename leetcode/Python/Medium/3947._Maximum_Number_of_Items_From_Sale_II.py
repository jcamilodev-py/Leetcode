from collections import defaultdict
from typing import List


class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)

        fm = defaultdict(int)

        for f, _ in items:
            fm[f]+=1

        bonus = [0] * (n+1)

        for i in range(1, n+1):
            if not fm[i]:
                continue
            for j in range(i, n+1, i):
                bonus[i]+=fm[j]

            bonus[i]-=1
        items.sort(key = lambda x: x[1])
        cheapest = items[0][1]

        ans = 0

        for f, p in items:
            if p >= cheapest * 2:
                break
            count = min(bonus[f], budget // p)
            ans+= count * 2
            budget-= count * p

        return ans + budget // cheapest





s = Solution()
print(s.maximumSaleItems([[1,6],[2,4],[3,5]], budget = 19))