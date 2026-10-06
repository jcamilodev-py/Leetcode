from math import gcd


class Solution:
    def subarrayGCD(self, nums: list[int], k: int) -> int:

        ans = 0
        n = len(nums)

        for i in range(n):
            v = nums[i]
            if v == k:
                ans+=1

            for j in range(i+1, n):
                v = gcd(nums[j], v)
                if v == k:
                    ans+=1

        return ans


s = Solution()
print(s.subarrayGCD([9,3,1,2,6,3], k = 3))