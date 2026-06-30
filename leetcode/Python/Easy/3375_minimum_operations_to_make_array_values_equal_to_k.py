from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
     if min(nums) < k:
        return -1
    
     mayores = set()
    
     for num in nums:
         if num > k:
             mayores.add(num)
     return len(mayores)
    
s = Solution()
print(s.minOperations([5,2,5,4,5], 2))