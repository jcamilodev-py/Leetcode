from typing import List

class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        startValue = 1
        current_Sum = 1
        i = 0
        while i < len(nums):
            if current_Sum + nums[i] >= 1:
                current_Sum = current_Sum + nums[i]
                i+=1
            else:
                startValue+=1
                current_Sum = startValue
                i = 0
        return startValue

        



s = Solution()
print(s.minStartValue([1,-2,-3]))