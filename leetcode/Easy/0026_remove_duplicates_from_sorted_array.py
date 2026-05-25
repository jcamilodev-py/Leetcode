from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        j = 1
        while j<= len(nums)-1:
            if nums[i] == nums[j]:
                del nums[i]
            else:
                i+=1
                j+=1
        return len(nums)


s = Solution()
print(s.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
