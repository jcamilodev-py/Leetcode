from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()

        return (nums[-1]-1) * (nums[-2]-1)




s = Solution()
print(s.maxProduct([3,4,5,2]))