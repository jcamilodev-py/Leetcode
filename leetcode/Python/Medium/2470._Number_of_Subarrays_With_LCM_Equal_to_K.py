from math import gcd


class Solution:
    def subarrayLCM(self, nums: list[int], k: int) -> int:
        ans = 0

        n = len(nums)

        for i in range(n):
            v = 1

            for j in range(i, n):
                v = v // gcd(v, nums[j]) * nums[j]

                if v == k:
                    ans+=1

        return ans




s = Solution()
print(s.subarrayLCM([3,6,2,7,1], k = 6))