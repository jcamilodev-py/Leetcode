class Solution:
    def minDeletions(self, nums: list[int]) -> int:
        ans = 0

        n = len(nums)

        for i in range(n-1):
            if nums[i] == nums[i+1]:
                ans+=1


        return ans





s = Solution()
print(s.minDeletions([1,1,2,2,2,3]))