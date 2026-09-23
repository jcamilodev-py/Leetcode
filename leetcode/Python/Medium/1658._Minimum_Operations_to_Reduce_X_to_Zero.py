class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:

        target = sum(nums) - x
        n = len(nums)

        current_sum = 0
        ans = -1

        l = 0

        for r in range(n):
            current_sum+=nums[r]

            while l <= r and current_sum > target:
                current_sum-=nums[l]
                l+=1

            if current_sum == target:
                ans = max(ans, r - l + 1)

        return n - ans if ans != -1 else -1




s = Solution()
print(s.minOperations([5,2,3,1,1], 5))