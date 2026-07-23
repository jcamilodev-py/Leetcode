class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.split()

        return len(s[-1])


s = Solution()
print(s.lengthOfLastWord("   fly me   to   the moon  "))