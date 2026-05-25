from typing import List


class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        if nums:
            r = list(range(min(nums), max(nums)+1))
            output = []
            for i in r:
                    if i not in r:
                      output.append(i)
            return output
        return []
        # nums.sort()
        # lista = []
        # for i in range(len(nums)-1):
        #     if nums[i]+1 == nums[i+1]:
        #         continue
        #     else:
        #         lista.append(nums[i+1]-1)
        # return lista



s = Solution()
print(s.findMissingElements([5,1]))