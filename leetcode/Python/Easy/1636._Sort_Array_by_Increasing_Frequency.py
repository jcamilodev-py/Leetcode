from typing import List
from collections import Counter

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        ans = []
        nums.sort()
        count = Counter(nums)
        
        for i,j in reversed(count.most_common()):
            for l in range(j):
                ans.append(i)

        return ans     
            

s = Solution()
print(s.frequencySort([1,5,0,5]))