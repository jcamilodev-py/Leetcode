from typing import List

class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        ans = 0

        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if words[i] == words[j][0:len(words[i])] and words[i] == words[j][0-len(words[i]):]:
                    ans+=1
        return ans


s = Solution()
print(s.countPrefixSuffixPairs(["pa","papa","ma","mama"]))