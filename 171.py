from typing import List

class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        value = 0
        for i in num:
            value = value *10 + i
        value+=k
        if value == 0:
            res = '0'
        else:
            digits = []
            while value > 0:
                digits.append(chr(ord('0') + value % 10))
                value //= 10
            digits.reverse()
            res = ''.join(digits)
        ans = []
        for i in res:
            ans.append(int(i))
        return ans
            
            




s = Solution()
print(s.addToArrayForm([1,2,0,0], 34))