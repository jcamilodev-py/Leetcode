from typing import List

class Solution:
    def constructRectangle(self, area: int) -> List[int]:

        for i in range(1, int(area*0.5) + 1):
            b = area // i
            if area % i == 0 and i >= b:
                
                return [i, b]
        
        if area % 2 != 0:
            return [area, 1]
        elif area == 2:
            return [2,1]


        


s = Solution()
print(s.constructRectangle(3))