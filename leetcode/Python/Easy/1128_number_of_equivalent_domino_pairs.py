from typing import List
# from typing import Counter


class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        dic = {}
        count = 0
        
        for i in dominoes:
            i.sort()
            if tuple(i) not in dic:
              dic[tuple(i)] = 1
            else:
                dic[tuple(i)]+=1

        for j in dic.values():
            j= int(j*(j-1) / 2)
            count+=j
        
        return count

s = Solution()
print(s.numEquivDominoPairs([[1,2],[3,1],[2,1],[1,3],[2,2]]))