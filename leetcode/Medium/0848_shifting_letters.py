from typing import List

class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        su = sum(shifts)
        ans = []

        for i in range(len(s)):

            total = ((ord(s[i]) - ord("a")) + su) % 26

            ans.append(chr(97 + total))
            su-=shifts[i]
        
        return "".join(ans)



s = Solution()
print(s.shiftingLetters("ruu", [26,9,17]))