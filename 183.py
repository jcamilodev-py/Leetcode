from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ans = []
        r = list(range(1, len(nums)+1))
        seen = set(nums)

        for i in r:
            if i not in seen:
                ans.append(i)
        return ans

s = Solution()
print(s.findDisappearedNumbers([1,1]))