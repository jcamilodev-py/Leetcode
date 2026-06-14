from typing import List
from collections import Counter

class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        n = len(words)
        i = 1

        while i < n:
            if Counter(words[i]) == Counter(words[i-1]):
                del words[i]
                n-=1
            else:
                i+=1
                
        return words 



s = Solution()
print(s.removeAnagrams(["a","b","c","d","e"]))