from typing import List
from collections import deque

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        min_d = deque()
        max_d = deque()
        l = 0
        ans = 0
        for i in range(len(nums)):
                while min_d and nums[i] < min_d[-1]:
                    min_d.pop()
                
                while max_d and nums[i] > max_d[-1]:
                    max_d.pop()

                min_d.append(nums[i])
                max_d.append(nums[i])

                while max_d[0] - min_d[0] > limit:
                    if nums[l] == max_d[0]:
                         max_d.popleft()
                    
                    if nums[l] == min_d[0]:
                        min_d.popleft()
                    l+=1
                ans = max(ans, i - l + 1)
        return ans



s = Solution()
print(s.longestSubarray(nums = [8,2,4,7], limit = 4))        