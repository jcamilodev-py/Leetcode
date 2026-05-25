class Solution:
    def busyStudent(self, startTime, endTime, queryTime):
        output = 0
        for i in range(len(startTime)):
            if startTime[i] <= queryTime and queryTime <= endTime[i]:
                output+=1

        return output





s = Solution()
print(s.busyStudent([1,2,3], [3,2,7], 4))


# output = 1
        