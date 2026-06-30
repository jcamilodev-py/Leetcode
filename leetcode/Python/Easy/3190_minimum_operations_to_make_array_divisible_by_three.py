from typing import List

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        operations = 0
        for i in nums:
            if (i + 1) % 3 == 0:
                i+=1
                operations+=1
            elif (i - 1) % 3 == 0:
                i-=1
                operations+=1
        return operations

s = Solution()
print(s.minimumOperations([1,3,4,5,6,7,8,8,8,9]))