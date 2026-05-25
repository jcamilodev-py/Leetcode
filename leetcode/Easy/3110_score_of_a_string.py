class Solution:
    def scoreOfString(self, s: str) -> int:
        l = []
        for i in range(len(s)-1):
            l.append(abs(ord(s[i]) - ord(s[i+1])))
        
        return sum(l)



s = Solution()
print(s.scoreOfString("zaz"))