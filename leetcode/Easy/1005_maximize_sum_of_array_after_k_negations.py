from typing import List

class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()
        for i,j in enumerate(nums):
            if j < 0:
                if k > 0:
                    nums[i] = abs(j)
                    k-=1
                else:
                    break
        nums.sort()
            
        while k > 0:
            if nums[0] < 0:
                nums[0] = abs(nums[0])
                k-=1
            else:
                nums[0] = -abs(nums[0])
                k-=1

        return sum(nums)


s = Solution()
print(s.largestSumAfterKNegations([2,-3,-1,5,-4], k = 2))