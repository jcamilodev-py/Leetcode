class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()

        n = len(nums)
        if n % 2 == 0:
            return sum(nums[n//2:]) - sum(nums[:n//2])
        
        return sum(nums[(n//2)+1:]) - sum(nums[:n//2])





s = Solution()
print(s.minMoves2([1,2,3]))