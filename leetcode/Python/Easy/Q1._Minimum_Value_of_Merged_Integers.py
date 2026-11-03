class Solution:
    def minMergedInteger(self, nums: list[int]) -> int:
        ans = float('inf')
        n = len(nums)

        for i in range(1, n, 2):
                v = str(nums[i-1]) + str(nums[i])
                ans = min(ans, int(v))


        return ans




s = Solution()
print(s.minMergedInteger([23,55,42,21]))