class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        new_s = ""
        for i in reversed(s):
            new_s +=i
            new_s += " "

        return new_s[:len(new_s)-1]
        

s = Solution()
print(s.reverseWords("a good   example"))