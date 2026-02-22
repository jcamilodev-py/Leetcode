from typing import List


class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()

        output = []
        for i,j in enumerate(nums):
            if j == target:
                output.append(i)

        return output



s = Solution()
print(s.targetIndices([1,2,5,2,3],  5))