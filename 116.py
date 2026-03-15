from typing import List


class Solution:
    def findLucky(self, arr: List[int]) -> int:
        dic = {}
        for i in arr:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] +=1
        
        ans = -1
        for i,j in dic.items():

            if i == j and i > ans:
                ans = i
        return ans
        


s = Solution()
print(s.findLucky([2,2,2,3,3]))