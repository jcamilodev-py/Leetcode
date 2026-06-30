from typing import List


class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        output = []
        dic = {}

        for i,j in zip(heights, names):
            dic[i] = j

        for x in range(len(names)):
            output.append(dic[max(dic)])
            del dic[max(dic)]
        return output



s = Solution()
print(s.sortPeople(["Mary","John","Emma"], [180,165,170]))