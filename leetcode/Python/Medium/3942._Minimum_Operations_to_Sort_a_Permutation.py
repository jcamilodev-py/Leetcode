from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        
        def h(nums):
            k = nums.index(0)

            for i in range(n):
                if nums[i] != (i - k) % n:
                    return -1

            return k

        candidate1, candidate2 = h(nums), h(list(reversed(nums)))

        candidates = []
        if candidate1 != -1:
            candidates.append(min(candidate1, (n - candidate1) % n + 2))
            
        if candidate2 != -1:
            candidates.append(min(candidate2, (n - candidate2) % n) + 1)

        return min(candidates) if candidates else -1


            

s = Solution()
print(s.minOperations([0,2,1]))
