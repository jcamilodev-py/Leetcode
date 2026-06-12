from typing import List
from collections import Counter

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1, s2 = s1.split(), s2.split()
        c1, c2 = Counter(s1), Counter(s2)
        
        ans = []

        for i in c1:
            if c1[i] == 1 and i not in c2:
                ans.append(i)
        for i in c2:
            if c2[i] == 1 and i not in c1:
                ans.append(i)
        
        return ans
        


s = Solution()
print(s.uncommonFromSentences("this apple is sweet", "this apple is sour"))

# Output: ["sweet","sour"]