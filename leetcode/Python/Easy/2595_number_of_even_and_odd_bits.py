from typing import List

class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        b = []
        while n > 0:
            b.append(n % 2)
            n = n // 2

        even = 0
        odd = 0
        for i,j in enumerate(b):
            print(b, even, odd)
            if i % 2 == 0 and j ==1:
                even+= 1
            elif i % 2 != 0 and j == 1:
                odd+=1

        return [even, odd]


s = Solution()
print(s.evenOddBit(2))