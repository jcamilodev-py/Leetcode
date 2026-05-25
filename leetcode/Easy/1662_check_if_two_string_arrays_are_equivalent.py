from typing import List

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        l1 = []
        l2 = []

        for i in word1:
            l1.append(i)
        
        for i in word2:
            l2.append(i)
        
        return "".join(l1) == "".join(l2)



s = Solution()
print(s.arrayStringsAreEqual(["a", "cb"], word2 = ["ab", "c"]))