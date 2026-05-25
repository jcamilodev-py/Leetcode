from typing import Counter

class Solution:
    def maxDifference(self, s: str) -> int:
        count = Counter(s)
        odd = float('inf')
        even = 0
        for i in count.values():
            if i % 2 == 0 and i < odd:
                odd = i
            elif i % 2 != 0 and i > even:
                even = i
        return even - int(odd)




s = Solution()
print(s.maxDifference("mmsmsym"))