class Solution:
    def minimizedStringLength(self, s: str) -> int:
        seen = set(s)
        return len(seen)


s = Solution()
print(s.minimizedStringLength("aaabc"))
# "cbbd"
# "aaabc"
