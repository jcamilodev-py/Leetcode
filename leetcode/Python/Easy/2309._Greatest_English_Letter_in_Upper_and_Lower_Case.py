class Solution:
    def greatestLetter(self, s: str) -> str:

        seen = set(s)
        
        s.lower()
        set_lower = set(s)
        ans = ""
        for i in seen:
            v = chr(ord(i) - 32)
            if v in set_lower:
                ans = max(ans, v)
        
        return ans


s = Solution()

print(s.greatestLetter("arRAzFif"))