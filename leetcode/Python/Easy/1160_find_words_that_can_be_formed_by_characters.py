from typing import List
from collections import Counter

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars_count = Counter(chars)
        total = 0

        for word in words:
            word_count = Counter(word)
        
            valid = True
            for c in word_count:
                if word_count[c] > chars_count[c]:
                    valid = False
                    break
        
            if valid:
                total += len(word)
    
        return total


s = Solution()
print(s.countCharacters(["cat","bt","hat","tree"], "atach"))