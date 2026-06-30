class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i = 0
        j = 0
        while j<=len(needle)-1:
            if i > len(haystack)-1:
                return -1
            if haystack[i] == needle[j]:
                i+=1
                j+=1
            else:
                i-=j
                i+=1
                j= 0
        return i-j
    
s = Solution()
print(s.strStr("sosa", "sa"))