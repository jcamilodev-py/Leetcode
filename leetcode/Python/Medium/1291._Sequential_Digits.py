from typing import List
from collections import deque

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ans = []
        d = deque(range(1, 10))

        while d:
            n = d.popleft()

            if n > high:
                continue
            
            o = n % 10
            if o < 9:
                v = n * 10 + (o + 1)
                d.append(v)

                if low <= v <= high:
                    ans.append(v)
                elif v > high:
                    return ans
            
        return ans



s = Solution()
print(s.sequentialDigits(low = 100, high = 300))