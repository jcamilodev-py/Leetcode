from math import comb


class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        mod = 10 ** 9 + 7

        def re(arr):
            if len(arr) <= 2:
                return 1

            root = arr[0]
            l = [i for i in arr if i < root]
            r = [i for i in arr if i > root]
            return comb(len(arr) - 1, len(l)) * re(l) % mod * re(r) % mod

        return (re(nums) - 1) % mod



s = Solution()
print(s.numOfWays([2,1,3]))