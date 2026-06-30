from typing import List

class Solution:
    def sortArrayByParityII(self, nums: List[int]):
        i = 0  
        j = 1  
        n = len(nums)

        while i < n and j < n:
            if nums[i] % 2 == 0:
                i += 2
            elif nums[j] % 2 == 1:
                j += 2
            else:
                nums[i], nums[j] = nums[j], nums[i]

        return nums

s = Solution()
print(s.sortArrayByParityII([4,2,5,7]))

# Input: nums = [4,2,5,7]
# Output: [4,5,2,7]
# Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.