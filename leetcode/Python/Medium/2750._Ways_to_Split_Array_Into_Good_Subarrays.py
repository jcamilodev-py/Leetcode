from typing import List


class Solution:
    def numberOfGoodSubarraySplits(self, nums: List[int]) -> int:
        mod = 10 ** 9 + 7   
        n = len(nums)
        ans = 1
        prev = -1

        for i in range(n):
            if nums[i] == 1:
                if prev != -1:
                    ans = ans * (i - prev) % mod
                prev = i

        return ans if prev != -1 else 0




s = Solution()
print(s.numberOfGoodSubarraySplits([0,1,1,0,1,1,1,0,1,1,1,0,1,1,1]))