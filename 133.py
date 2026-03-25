from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = len(nums)-1
        for i in range(len(nums)-2, -1, -1):

            if nums[i] == nums[j] and nums[i] == nums[i-1] and i-1 >=0:
                del nums[j]
                j-=1
            else:
                j-=1

        return len(nums)
                


s = Solution()
print(s.removeDuplicates([0,0,1,1,1,1,2,3,3]))
# Input: nums = [1,1,1,2,2,3]
# Output: 5, nums = [1,1,2,2,3,_]