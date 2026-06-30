from typing import List

class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        dic = {

        }
        for i in rectangles:
            j = min(i)
            if j not in dic:
                dic[j] = 1
            else:
                dic[j]+=1
        
        m = max(dic)
        return dic[m]



s = Solution()
print(s.countGoodRectangles([[2,3],[3,7],[4,3],[3,7]]))