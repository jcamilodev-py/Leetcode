from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        ban_r, ban_d, d, r = 0,0,0,0
        q = deque(senate)
        for i in senate:
            if i == "D":
                d+=1
            else:
                r+=1

        while d and r:
            i = q.popleft()
            if i == "D":
                if ban_d == 0:
                    ban_r+=1
                    q.append(i)
                else:
                    d-=1
                    ban_d-=1
                    continue
            elif ban_r == 0:
                ban_d+=1
                q.append(i)
            else:
                r-=1
                ban_r-=1
                continue
        return "Radiant" if r > d else "Dire"


s = Solution()
print(s.predictPartyVictory("DDRRR"))