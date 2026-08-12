class Solution:
    def validPalindrome(self, s: str) -> bool:
        s = list(s)
        n = len(s)
        i, j = 0, n-1

        while i < j:
            if s[i] != s[j]:
                break
            i+=1
            j-=1

        def is_palindrome(i, j, s):
            while i < j:
                if s[i] != s[j]:
                    return False
                i+=1
                j-=1

            return True

        c = s.copy()
        del c[i]
        del s[j]

        return is_palindrome(0, n-2, c) or is_palindrome(0, n-2, s)




s = Solution()
print(s.validPalindrome("aba"))