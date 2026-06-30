from typing import List


class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        dic = {}
        for i in nums:
            if i in dic:
                return i
            else:
                dic[i] =1


s = Solution()
print(s.repeatedNTimes([2,1,2,5,3,9]))