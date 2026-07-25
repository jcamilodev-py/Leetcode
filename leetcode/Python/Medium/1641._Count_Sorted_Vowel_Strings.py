from math import comb

class Solution:
    def countVowelStrings(self, n: int) -> int:

        return comb(n+4, n)
    

s = Solution()
print(s.countVowelStrings(33))