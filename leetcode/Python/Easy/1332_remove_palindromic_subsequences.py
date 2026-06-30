class Solution:
    def removePalindromeSub(self, s: str) -> int:
        i,j = 0, len(s)-1
        while i < j:
            if s[i] == s[j]:
                i+=1
                j-=1
            else:
                return 2
        return 1

s = Solution()
print(s.removePalindromeSub("babababbababab"))