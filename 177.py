from typing import List

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        current_max = 0
        current = 0
        for i in gain:
            current = current + i
            if current > current_max:
                current_max = current

        return current_max


s = Solution()
print(s.largestAltitude([-4,-3,-2,-1,4,3,2]))