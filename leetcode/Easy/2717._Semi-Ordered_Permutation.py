from typing import List

class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        i = nums.index(1)
        j = n-1

        while nums[0] != 1:
            nums[i], nums[i-1] = nums[i-1], nums[i]
            ans+=1
            i-=1
        
        while nums[j] != n:
            ans+=1
            j-=1
        
        return ans





s = Solution()
print(s.semiOrderedPermutation([2,1,4,3]))