class Solution:
    def countAsterisks(self, s: str) -> int:
        ans, count = 0, 0

        for i in s:
            if count == 0 and i == "*":
                ans+=1

            if i == "|":
                count+=1
            
            if count == 2:
                count = 0
        
        return ans



s = Solution()
print(s.countAsterisks("yo|uar|e**|b|e***au|tifu|l"))