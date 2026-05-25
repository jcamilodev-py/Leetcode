from typing import List

class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        seen = {"a","e","i","o","u","A","E","I","O","U"}
        a = []
        length = len(words)

        for i in range(length):
            if words[i][0] in seen and words[i][-1] in seen:
                a.append(1)
            else:
                a.append(0)
        
        
        p = [0] * (length + 1)
        for i in range(1, length+1):
            p[i] = p[i - 1] + a[i - 1]
        
        
        ans = []
        for i in queries:
            ans.append(p[i[1]+1] - p[i[0]])

        return ans
   

s = Solution()
print(s.vowelStrings(["aba","bcb","ece","aa","e"], queries = [[0,2],[1,4],[1,1]]))