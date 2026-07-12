class Solution:
    def secondsBetweenTimes(self, startTime: str, endTime: str) -> int:
        s1 = int(startTime[:2]) * 3600 + int(startTime[3:5]) * 60 + int(startTime[6:])

        s2 = int(endTime[:2]) * 3600 + int(endTime[3:5]) * 60 + int(endTime[6:])

        return s2 - s1



s = Solution()
print(s.secondsBetweenTimes("12:34:56", "13:00:00"))