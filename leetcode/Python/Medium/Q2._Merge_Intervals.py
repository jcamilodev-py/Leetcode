from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        i = 0
        n = len(intervals)-1
        while i < n:
            if intervals[i][1] >= intervals[i+1][0]:
                intervals[i+1][0] = min(intervals[i][0], intervals[i+1][0])
                intervals[i+1][1] = max(intervals[i][1], intervals[i+1][1])
                del intervals[i]
                n-=1
            else:
                i+=1
        return intervals


s = Solution()
print(s.merge([[1,4],[2,3]]))

# [[1,3],[2,6],[8,10],[15,18]]
# [[1,4],[4,5]]
