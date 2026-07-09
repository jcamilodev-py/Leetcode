class Solution:
    def longestPalindrome(self, s: str) -> str:
        def exp(s, l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l-=1
                r+=1
            return l+1, r-1
        
        st, e = 0, 0

        for i in range(len(s)):
            l1, r1 = exp(s, i, i)
            l2, r2 = exp(s, i, i+1)

            if r1 - l1 +1 > e - st+1:
                st, e = l1, r1
            
            if r2 - l2 +1 > e - st+1:
                st, e = l2, r2
        
        return s[st: e+1]


s = Solution()
print(s.longestPalindrome("babad"))