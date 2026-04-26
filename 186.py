from typing import List

class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        dic = {}

        for i in nums:
            if i % 2 == 0:
                if i in dic:
                    dic[i]+=1
                else:
                    dic[i] = 1
        if not dic:
            return -1
        m = max(dic.values())
        order = dict(sorted(dic.items()))
        for i,j in order.items():
            if j == m:
                return i

s = Solution()
print(s.mostFrequentEven([29,47,21,41,13,37,25,7]))