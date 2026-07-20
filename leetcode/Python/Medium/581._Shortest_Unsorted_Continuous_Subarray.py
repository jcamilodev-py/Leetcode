from typing import List

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        sorted_nums = sorted(nums)
        i, j = 0, n-1

        vi, vj = False, False
        while i < j:
            if nums[i] != sorted_nums[i]:
                v1 = i
                vi = True
            else:
                i+=1
            
            if nums[j] != sorted_nums[j]:
                v2 = j
                vj = True
            else:
                j-=1
            
            if vi and vj:
                return (v2 - v1) +1

        return 0



s = Solution()
print(s.findUnsortedSubarray([2,6,4,8,10,9,15]))