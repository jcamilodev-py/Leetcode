from typing import List, Counter

class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        count1 = Counter(words1)
        count2 = Counter(words2)
        ans = 0
        for i, j in count1.items():
            if j == 1 and i in count2:
                if count2[i] == 1:
                    ans+=1
        return ans 
        


s = Solution()
print(s.countWords(words1 = ["a","ab"], words2 = ["a","a","a","ab"]))