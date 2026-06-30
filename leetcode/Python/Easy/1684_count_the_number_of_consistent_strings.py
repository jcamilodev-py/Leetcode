from typing import List


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0
        seen = [''.join(set(palabra)) for palabra in words]

        for i in range(len(seen)):
            for j in range(len(seen[i])):
                if seen[i][j] not in allowed:
                    break
                else:
                  if j == len(seen[i])-1:
                      count+=1
        return count




s = Solution()
print(s.countConsistentStrings("cad", ["cc","acd","b","ba","bac","bad","ac","d"]))
