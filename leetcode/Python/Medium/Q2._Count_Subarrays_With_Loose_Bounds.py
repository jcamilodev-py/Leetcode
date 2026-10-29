class Solution:
    def countSubarrays(self, nums: list[int], minK: int, maxK: int) -> int:
        n = len(nums)
        i,j = 0, 0
        ans = 0

        while j < n:
            if nums[j] <= maxK and nums[j] >= minK:
                ans+= j - i + 1
                j+=1
            else:
                j+=1
                i = j

        return ans





s = Solution()
print(s.countSubarrays([1,4,7,3], minK = 1, maxK = 5))