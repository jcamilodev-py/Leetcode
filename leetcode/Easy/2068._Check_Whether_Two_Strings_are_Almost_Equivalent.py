from collections import Counter

class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        c1 = Counter(word1)
        c2 = Counter(word2)

        for i in c1:
            if i in c2:
                if abs(c2[i] - c1[i]) > 3:
                    return False
            elif c1[i] > 3:
                return False
        
        for j in c2:
            if j in c1:
                if abs(c2[j] - c1[j]) > 3:
                    return False
            elif c2[j] > 3:
                return False
            
            
        return True

s = Solution()
print(s.checkAlmostEquivalent("abacccc", "aababaa"))