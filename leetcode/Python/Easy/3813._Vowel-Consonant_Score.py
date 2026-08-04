class Solution:
    def vowelConsonantScore(self, s: str) -> int:
        vowels = set({"a","e","i","o","u"})
        numbers = set({"1","2","3","4","5","6","7","8","9","0"})
        v = 0
        c = 0

        for i in s:
            if i in vowels:
                v+=1
            else:
                if i != " " and i not in numbers:
                    print(i)
                    c+=1

        
        return v // c if c > 0 else 0




s = Solution()
print(s.vowelConsonantScore("i3"))