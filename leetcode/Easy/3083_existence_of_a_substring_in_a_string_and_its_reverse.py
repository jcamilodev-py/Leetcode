class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        map = {

        }
        for i in range(len(s)-1):
            if s[i:i+2] is not map:
                map[s[i:i+2]] = 1
        rev = s[::-1]
        for j in range(len(rev)-1):
            if rev[j:j+2] in map:
                return True
        return False


s = Solution()
print(s.isSubstringPresent("leetcode"))