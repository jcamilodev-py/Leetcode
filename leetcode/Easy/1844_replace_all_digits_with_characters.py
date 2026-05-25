class Solution:
    def replaceDigits(self, s: str) -> str:
        ans = []
        seen = set({'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'})
        for i,j in enumerate(s):
            if j in seen:
                ans.append(j)
            else:
                value = ord(s[i-1])
                ans.append(chr(value+int(j)))
        
        return "".join(ans)


s = Solution()
print(s.replaceDigits("a1c1e1"))