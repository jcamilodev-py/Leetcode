class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        text_s = ''.join(sorted(s))
        text_t = ''.join(sorted(t))
        for i,j in enumerate(text_s):
            if text_s[i] != text_t[i]:
                return text_t[i]
        return text_t[-1]


s = Solution()
print(s.findTheDifference("", t = "y"))