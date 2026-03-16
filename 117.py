from typing import List

class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:

        ans = max(nums)
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[j] > nums[j-1]:
                    if sum(nums[i:j+1]) > ans:
                        ans = sum(nums[i:j+1])
                else:
                    break
        return ans

s = Solution()
print(s.maxAscendingSum([9,1,3,4]))