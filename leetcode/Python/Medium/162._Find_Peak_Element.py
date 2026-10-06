class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        return nums.index(max(nums))




s = Solution()
print(s.findPeakElement([1,2,3,1]))