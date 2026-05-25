from typing import List

class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        for i,j in enumerate(nums):
            if j %2 == 0:
                nums[i] = 0
            else:
                nums[i] = 1

        return sorted(nums)
    
s = Solution()
print(s.transformArray([4,3,2,1]

))