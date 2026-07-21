from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        c = Counter(magazine)
        c2 = Counter(ransomNote)
        for i in c2:
            if i not in c or c2[i] > c[i]:
                return False
        
        return True

    
s = Solution()
print(s.canConstruct(ransomNote = "aa", magazine = "aba"))