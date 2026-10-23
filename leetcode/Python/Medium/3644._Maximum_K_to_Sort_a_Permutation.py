from typing import List


class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        k = 0

        for i in range(len(nums)):
            if nums[i] != i:
                if nums[i] == 0:
                    return 0
                if k != 0:
                    k&=nums[i]
                    if k== 0:
                        return 0
                else:
                    k = nums[i]
                

        return k

s = Solution()
print(s.sortPermutation([2,0,1]))

