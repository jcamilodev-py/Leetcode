from typing import List


class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()
        i,j = 0, len(nums)-1

        while i < j:
            if nums[i] + nums[j] == 0:
                return abs(nums[i])
            
            elif abs(nums[i]) < nums[j]:
                j-=1
            else:
                i+=1
        return -1


s = Solution()
print(s.findMaxK([-10,8,6,7,-2,-3]))