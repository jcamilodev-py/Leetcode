class Solution:
    def minMoves(self, nums: list[int]) -> int:
        v = min(nums)
        ans = 0

        for i in nums:
            ans+=i-v

        return ans

            




s = Solution()
print(s.minMoves([1,2,3]))