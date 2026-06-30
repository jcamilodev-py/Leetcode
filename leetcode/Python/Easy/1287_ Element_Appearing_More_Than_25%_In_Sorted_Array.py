from typing import List

class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        c = (len(arr) * 25 )//100
        dic = {}

        for i in arr:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] +=1

            if dic[i] > c:
                return i


s = Solution()
print(s.findSpecialInteger([1,1]))