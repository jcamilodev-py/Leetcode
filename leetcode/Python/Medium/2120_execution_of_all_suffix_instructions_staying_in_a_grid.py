from typing import List

class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        ans = []

        for i in range(len(s)):
            start = startPos.copy()
            count = 0
            for j in range(i, len(s)):

                match s[j]:
                    case "R":
                        if not start[1] +1 < n:
                            break

                        count+=1
                        start[1] +=1
                    case "L":
                        if not start[1] -1 >= 0:
                            break
                        count+=1
                        start[1] -=1
                    case "D":
                        if not start[0] +1 < n:
                            break

                        count+=1
                        start[0] +=1
                    case "U":
                        if not start[0] -1 >= 0:
                            break

                        count+=1
                        start[0] -=1

            ans.append(count)
                
        return ans


s = Solution()
print(s.executeInstructions(n = 3, startPos = [0,1], s = "RRDDLU"))