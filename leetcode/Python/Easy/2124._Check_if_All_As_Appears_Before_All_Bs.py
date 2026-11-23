class Solution:
    def checkString(self, s: str) -> bool:
        b = -1

        for i in range(len(s)):
            if s[i] == "b" and b == -1:
                b = i
            if s[i] == "a" and b != -1:
                return False
        return True




s = Solution()
print(s.checkString("aaabbb"))