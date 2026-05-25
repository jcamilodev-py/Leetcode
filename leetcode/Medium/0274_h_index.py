from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        h = 0
        citations = sorted(citations)
        for i in range(len(citations)-1, -1, -1):
            if citations[i] >= h+1:
                h+=1
            else:
                return h
        return h


# 0,1,3,5,6
s = Solution()
print(s.hIndex([0]))