from typing import List

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        n = len(s)
        seen = set({})
        ans = [0]
        distance = 0
        for i in range(n):
            j = n-1
            su = sum(ans)
            while True:

                if i - su == distance -1:
                    ans.append(distance)
                    distance = 0
                    break

                if s[i] in seen:
                    break

                elif s[i] == s[j]:
                    if (j - su) + 1 > distance:
                        distance = (j - su) + 1
                        seen.add(s[i])
                        if i - su == distance -1:
                            ans.append(distance)
                            distance = 0
                        break
                    break


                else:
                    j-=1

        return ans[1:]



s = Solution()
print(s.partitionLabels("eccbbbbdec"))