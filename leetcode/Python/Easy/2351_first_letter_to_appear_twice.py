class Solution:
    def repeatedCharacter(self, s: str) -> str:
        dic = {}
        for i in s:
            if i in dic:
                return i
            dic[i] = None
            
            


s = Solution()
print(s.repeatedCharacter("abca"))