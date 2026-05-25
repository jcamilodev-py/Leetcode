from typing import List

class Solution:
    def smallestAbsent(self, nums: List[int]) -> int:
        n, s = 0,0
        for i in nums:
            n+=1
            s+=i
        seen = set(nums)
        value = s/n
        ans = 1
        while ans <= value or ans in seen:
            ans+=1

        return ans



s = Solution()
print(s.smallestAbsent([4,-1]))