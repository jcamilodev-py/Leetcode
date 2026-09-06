class Solution:
    def countRotations(self, s: str, k: int) -> int:
        n = len(s)

        c = 0
        for i in range(n-1):
            if s[i] == s[i+1]:
                c+=1

        if s[-1] == s[0]:
            c+=1

        if k == c:
            return n - c
        elif k == c-1:
            return c
        
        return 0


s = Solution()
print(s.countRotations("aab", k = 1))