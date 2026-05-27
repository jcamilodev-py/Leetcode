from typing import List

class Solution:
    def countStableSubarrays(self, capacity: List[int]) -> int:
        n = len(capacity)

        p = [0] * (n + 1)
        for i in range(n):
            p[i + 1] = p[i] + capacity[i]

        seen = {}
        ans = 0

        for r in range(2, n):
            l = r - 2

            key_l = (p[l + 1], capacity[l])
            seen[key_l] = seen.get(key_l, 0) + 1

            target = (p[r] - capacity[r], capacity[r])
            ans += seen.get(target, 0)

        return ans


s = Solution()
print(s.countStableSubarrays([-4,4,0,0,-8,-4]))