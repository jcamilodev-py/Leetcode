from typing import List

class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        operations = 0

        def not_decreasing(arr):
            for i in range(1, len(arr)):
                if arr[i] < arr[i-1]:
                    return False
            return True

        while not not_decreasing(nums):
            min_sum = float('inf')
            idx = 0

            for i in range(len(nums) - 1):
                s = nums[i] + nums[i+1]
                if s < min_sum:
                    min_sum = s
                    idx = i

            nums = nums[:idx] + [nums[idx] + nums[idx+1]] + nums[idx+2:]
            operations += 1

        return operations
            

s = Solution()
print(s.minimumPairRemoval([5,2,3,1]))
