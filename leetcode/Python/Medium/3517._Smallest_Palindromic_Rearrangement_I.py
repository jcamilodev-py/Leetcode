from collections import Counter

class Solution:
    def smallestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 1:
            return s
        s = sorted(s)
        
        c = Counter(s)
        ans = [0] * n

        i = 0

        h = ""
        for x in c:
            while c[x] > 1:
                ans[i] = x
                ans[(n-1) - i] = x
                i+=1
                c[x]-=2

            if c[x] == 1:
                h = x

        if h:
            ans[n // 2] = h 

        return "".join(ans)



s = Solution()
print(s.smallestPalindrome("rur"))