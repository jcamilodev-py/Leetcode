class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        count = 0

        for i in range(len(s)-1):
            if s[i] != s[i+1]:
                count+=1
        return count <2
            


s = Solution()
print(s.checkOnesSegment("110"))