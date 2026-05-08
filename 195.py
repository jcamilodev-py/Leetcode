from typing import List

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        r = list(range(left, right+1))
        ans = []

        for i in r:

            n = i
            
            b = True
            while n > 0:
                digito = n % 10
                if digito == 0:
                    b = False
                    break
                if i % digito != 0:
                    b = False
                    break
                n//=10

            if b:
                ans.append(i)

        return ans



s = Solution()
print(s.selfDividingNumbers(left = 47, right = 85))