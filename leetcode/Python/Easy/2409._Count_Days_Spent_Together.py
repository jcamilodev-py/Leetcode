m = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
ps = [0] * 13
for i in range(1, 13):
    ps[i] = ps[i-1] + m[i]

class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        a = ps[int(arriveAlice[:2]) - 1] + int(arriveAlice[3:])
        b = ps[int(leaveAlice[:2]) - 1] + int(leaveAlice[3:])
        c = ps[int(arriveBob[:2]) - 1] + int(arriveBob[3:])
        d = ps[int(leaveBob[:2]) - 1] + int(leaveBob[3:])

        ans = min(b, d) - max(a, c) + 1
        return max(ans, 0)


s = Solution()
print(s.countDaysTogether(arriveAlice = "10-01", leaveAlice = "10-31", arriveBob = "11-01", leaveBob = "12-31"))