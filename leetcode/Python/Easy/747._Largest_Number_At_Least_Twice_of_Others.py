from typing import List

class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        dic = {}
        for i,j in enumerate(nums):
            dic[j] = i

        nums.sort()
        
        if nums[-1] // 2 >= nums[-2]:
            return dic[nums[-1]]
        return -1


s = Solution()
print(s.dominantIndex([1,2,3,4]))