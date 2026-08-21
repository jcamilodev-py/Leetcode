from bisect import bisect_left

class ExamTracker:

    def __init__(self):
        self.p = [(0, 0)]

    def record(self, time: int, score: int) -> None:
        _, ps = self.p[-1]
        self.p.append((time, score + ps))

    def totalScore(self, startTime: int, endTime: int) -> int:
        l = bisect_left(self.p, ((startTime, -1)))
        r = bisect_left(self.p, ((endTime+1, -1)))

        _, a = self.p[l - 1]
        _, b = self.p[r - 1]


        return b - a
        
        

o = ExamTracker()
o.record(1, 98)
print(o.totalScore(1,1))
o.record(5,99)
print(o.totalScore(1,3))
print(o.totalScore(1, 5))
print(o.totalScore(3, 4))
print(o.totalScore(2, 5))


# Your ExamTracker object will be instantiated and called as such:
# obj = ExamTracker()
# obj.record(time,score)
# param_2 = obj.totalScore(startTime,endTime)