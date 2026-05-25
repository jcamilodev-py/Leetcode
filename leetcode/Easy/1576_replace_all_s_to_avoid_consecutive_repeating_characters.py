class Solution:
    def modifyString(self, s: str) -> str:
        s = list(s)

        for i in range(len(s)):
            if s[i] == "?":
                for ch in "abc":
                    prev_char = s[i-1] if i > 0 else ""
                    next_char = s[i+1] if i < len(s)-1 else ""

                    if ch != prev_char and ch != next_char:
                        s[i] = ch
                        break

        return "".join(s)



s = Solution()
print(s.modifyString("j?qg??b"))