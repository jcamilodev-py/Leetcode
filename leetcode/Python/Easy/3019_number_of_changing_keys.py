class Solution:
    def countKeyChanges(self, s: str) -> int:
        index = 0
        output = 0
        for i in range(1, len(s)):

           if abs(ord(s[index]) - ord(s[i])) == 32 or ord(s[index]) == ord(s[i]):
               index +=1
           else:
               index+=1
               output +=1 
        return output
               




s = Solution()
print(s.countKeyChanges("aAbBcC"))




# ord()
# chr()