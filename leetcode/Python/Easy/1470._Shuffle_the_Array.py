from typing import List

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = []
        for i in range(n):
            ans.append(nums[i])
            ans.append(nums[i + n])
        
        return ans




s = Solution()
print(s.shuffle([1,2,3,4,4,3,2,1], n = 4))