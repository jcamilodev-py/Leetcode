from typing import List

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        dic = {}
        ans = 0


        for i in range(len(reservedSeats)):
            if reservedSeats[i][0] not in dic:
                dic[reservedSeats[i][0]] = set()
                dic[reservedSeats[i][0]].add(reservedSeats[i][1])
            else:
                dic[reservedSeats[i][0]].add(reservedSeats[i][1])
        
        for i in dic.values():
            if 2 not in i and 3 not in i and 4 not in i and 5 not in i and 6 not in i and 7 not in i and 8 not in i and 9 not in i:
                ans+=2
            elif 2 not in i and 3 not in i and 4 not in i and 5 not in i:
                ans+=1
            elif 4 not in i and 5 not in i and 6 not in i and 7 not in i:
                ans+=1
            elif 6 not in i and 7 not in i and 8 not in i and 9 not in i:
                ans+=1
        
        return ans+(n - len(dic)) * 2



s = Solution()
print(s.maxNumberOfFamilies(n = 3, reservedSeats = [[1,2],[1,3],[1,8],[2,6],[3,1],[3,10]]
))