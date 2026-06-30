from typing import List

class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        for x, i in enumerate(matrix):
            m = min(i)
            row = [x]
            idx = i.index(m)

            
            add = True
            for y, j in enumerate(matrix):
                if row != y:
                    if m < j[idx]:
                        add = False
                        break
            if add:
                ans.append(m)
        
        return ans


s = Solution()
print(s.luckyNumbers([[3,7,8],[9,11,13],[15,16,17]]))