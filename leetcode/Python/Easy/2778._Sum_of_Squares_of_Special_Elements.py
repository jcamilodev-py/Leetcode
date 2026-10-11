class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)

        ans = 0

        for i in range(1, n+1):
            if not n % i:
                ans+=nums[i-1] ** 2

        return ans 




s = Solution()
print(s.sumOfSquares([2,7,1,19,18,3]))