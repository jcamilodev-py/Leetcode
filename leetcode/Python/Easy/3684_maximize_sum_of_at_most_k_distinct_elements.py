from typing import List


class Solution:
    def maxKDistinct(self, nums: List[int], k: int) -> List[int]:
        nums .sort()
        seen = set()
        for i in reversed(nums):
            if i not in seen:
                seen.add(i)
                if len(seen) >= k:
                    seen = list(seen)
                    return sorted(seen, reverse=True)
            
        seen = list(seen)
        return sorted(seen, reverse=True)




s = Solution()
print(s.maxKDistinct([84,93,100,77,93], 3))