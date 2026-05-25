from typing import List


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        i,j=0,1

        while j< len(nums):
            if nums[i] %2 !=0:
                if nums[j] %2 == 0:
                    nums[i], nums[j] = nums[j], nums[i]
                    i+=1
                    j+=1
                else:
                    j+=1
            else:
              i+=1
              j+=1
        return nums

s = Solution()
print(s.sortArrayByParity([0]))
# Output: [2,4,3,1]
# Input: nums = [0]
# Output: [0]