class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:
        nums.sort()

        dp = [0] * (max(nums)+2)

        for i in nums:
            dp[i+1] = max(dp[i+1], dp[i] + 1)
            dp[i] = max(dp[i], dp[i-1] + 1)

        return max(dp)




s = Solution()
print(s.maxSelectedElements([2,1,5,1,1]))