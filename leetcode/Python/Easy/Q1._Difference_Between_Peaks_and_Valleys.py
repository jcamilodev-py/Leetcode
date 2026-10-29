class Solution:
    def peakValleyDifference(self, nums: list[int]) -> int:
        n = len(nums)
        peak = 0
        valley = 0

        for i in range(1, n-1):
            if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
                peak+=nums[i]
            elif nums[i] < nums[i - 1] and nums[i] < nums[i + 1]:
                valley+=nums[i]

        return peak - valley





s = Solution()
print(s.peakValleyDifference([1,5,2,4,1,3,0]))