from typing import List

class Solution:
    def captureForts(self, forts: List[int]) -> int:
        i,j,n = 0,1, len(forts)
        ans, count = 0, 0

        while j < n:
            while forts[i] == 1 and forts[j] == 0 or forts[i] == -1 and forts[j] == 0:
                count+=1
                j+=1
                if j >= n:
                    return ans
            if forts[i] == 1 and forts[j] == -1:
                ans = max(ans, count)
            elif forts[i] == -1 and forts[j] == 1:
                ans = max(ans, count)
            
            i = j
            j = j+1
            count = 0
        
        return ans


s = Solution()
print(s.captureForts([-1,-1,1,-1,-1,0]))