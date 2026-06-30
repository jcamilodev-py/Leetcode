from typing import List

class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        nums.sort()

        m = 0
        for i in range(k):
            m+=nums[-1]
            nums[-1] = nums[-1] +1
        
        return m


s = Solution()
print(s. maximizeSum([1,2,3,4,5], k = 3))