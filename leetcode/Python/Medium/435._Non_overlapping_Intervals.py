class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort()
        ans = 0

        prev = intervals[0][1]

        for i, j in intervals[1:]:
            if i >= prev:
                prev = j
            else:
                ans+=1
                prev = min(prev, j)

        return ans



s = Solution()
print(s.eraseOverlapIntervals(intervals = [[1,2],[2,3],[3,4],[1,3]]))