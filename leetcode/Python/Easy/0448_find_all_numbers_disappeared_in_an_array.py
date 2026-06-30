from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        r = list(range(1, len(nums)+1))
        seen = set(nums)

        ans = [i for i in r if i not in seen]
        return ans

s = Solution()
print(s.findDisappearedNumbers([1,1]))