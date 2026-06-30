from typing import List

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        arr_sort = sorted(arr)
        ans = []
        dic = {}
        n = len(arr)

        r = list(range(n, 0, -1))

        for i in range(n):
            if arr_sort[i] not in dic:
                dic[arr_sort[i]] = r[-1]
                r.pop()

        for i in arr:
            ans.append(dic[i])
        
        return ans

        


s = Solution()
print(s.arrayRankTransform([37,12,28,9,100,56,80,5,12]))