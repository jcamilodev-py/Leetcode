from typing import List

class Solution:
    def lastVisitedIntegers(self, nums: List[int]) -> List[int]:
        seen = []
        ans = []
        k = 0
        lenght_seen = 0

        n = len(nums)

        for i in range(n):
            if nums[i] > 0:
                seen.insert(0, nums[i])
                lenght_seen+=1
                k = 0
            else:
                k+=1
                if k <= lenght_seen:
                    ans.append(seen[k-1])
                else:
                    ans.append(-1)
        
        return ans




s = Solution()
print(s.lastVisitedIntegers([1,2,-1,-1,-1]))