from typing import List

class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        ans = []
        current = []
        n = len(words)
        for i in range(n):

            for l, j in enumerate(words[i]):
                if j != separator:
                    current.append(j)
                else:
                    if current:
                        ans.append("".join(current))
                    current.clear()

                # print(l, len(words[i])-1)
                if l == len(words[i])-1:
                    if current:
                        ans.append("".join(current))
                    current.clear()

        return ans

        


s = Solution()
print(s.splitWordsBySeparator(["one.two.three","four.five","six"], "."))