from typing import List

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        s = []
        for i in arr:
            b = abs(i.bit_count())
            s.append((b,i))

        ans = []

        s.sort()
        for j in s:
            ans.append(j[1])
        
        return ans
        


s = Solution()
print(s.sortByBits(arr = [0,1,2,3,4,5,6,7,8]))