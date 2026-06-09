from typing import List
import heapq

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        ans = set()

        for i in nums:
            if i != 0:
                ans.add(i)
        
        return len(ans)
        




s = Solution()
print(s.minimumOperations([1,5,3,5]))