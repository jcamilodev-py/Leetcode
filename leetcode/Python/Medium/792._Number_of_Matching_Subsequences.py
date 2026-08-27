from typing import List
from collections import defaultdict
from bisect import bisect_left

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        d = defaultdict(list)
        
        for i, j in enumerate(s):
            d[j].append(i)

        ans = 0
        def ok(wordss, pos):
            for c in wordss:
                idx = bisect_left(d[c], pos)
                if idx == len(d[c]):
                    return False
                pos = d[c][idx]+1
            return True

        for i in words:
            if ok(i, 0):
                ans+=1

        return ans

           




s = Solution()
print(s.numMatchingSubseq(s = "abcde", words = ["a","bb","acd","ace"]))