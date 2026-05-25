from typing import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
       w1 = set(word1)
       w2 = set(word2)
       
       count1 = Counter(word1)
       count2 = Counter(word2)
       value = list(count1.values())
       value2 = list(count2.values())
       value.sort()
       value2.sort()

       return True if value == value2 and w1 == w2 else False
    
s = Solution()
print(s.closeStrings("uau", "ssx"))