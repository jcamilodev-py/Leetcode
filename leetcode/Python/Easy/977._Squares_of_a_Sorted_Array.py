from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n):
            nums[i] = nums[i]**2
        
        nums.sort()
        return nums


s = Solution()
print(s.sortedSquares([-4,-1,0,3,10]))