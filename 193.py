from typing import List

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        value1 = 1
        value2 = 1
        value1*= nums[-1]
        value1*= nums[-2]
        value1*=nums[-3]
        
        value2*= nums[0]
        value2*= nums[1]
        value2*= nums[-1]
        return max(value1, value2)
            

s = Solution()
print(s.maximumProduct([-100,-98,-1,2,3,4]))