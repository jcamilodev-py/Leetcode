from typing import List


class Solution:
    def sumZero(self, n: int) -> List[int]:
        r = n // 2
        ans = []

        for i in range(1, (r) + 1):
            ans.append(-i)

        def h(value):
            for i in range((n - r) - value, -value, -1):
                ans.append(i)

            return ans

        if n % 2 == 0:
            return h(0)
        return h(1)
            




s = Solution()
print(s.sumZero(4))