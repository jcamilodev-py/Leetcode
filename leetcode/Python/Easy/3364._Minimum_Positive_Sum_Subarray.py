from typing import List


class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)

        p = [0] * (n+1)

        for i in range(1, n+1):
            p[i] = p[i-1] + nums[i-1]


        ans = float('inf')

        for i in range(l, n+1):
            for j in range(max(0, i-r), i - l + 1):
                if p[i] - p[j] > 0 and p[i] - p[j] < ans:
                    ans = p[i] - p[j]

        return ans if ans != float('inf') else -1



s = Solution()
print(s.minimumSumSubarray([3, -2, 1, 4], l = 2, r = 3))