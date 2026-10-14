class BusBooking:

    def __init__(self, n: int):
        self.seen = set()
        self.min_time = 0
        self.total_time = 0
        self.windows = set()
        

    def toggle(self, seat: str) -> None:
        if seat not in self.seen:
            self.seen.add(seat)
            self.min_time+=1
            self.total_time+=1

            if seat[0] == "A":
                if "B" + seat[1:] in self.seen:
                    self.total_time+=2
                    self.windows.add(seat)
            elif seat[0] == "D":
                if "C" + seat[1:] in self.seen:
                    self.total_time+=2
                    self.windows.add("D" + seat[1:])
        else:
            self.seen.remove(seat)
            self.min_time-=1
            self.total_time-=1
            
            if seat in self.windows:
                self.total_time-=2
                self.windows.remove(seat)

    def getTotalTime(self) -> int:
        return self.total_time
        

    def getMinTime(self) -> int:
        return self.min_time
        

s = BusBooking(20)
print(s.toggle("C7"))
print(s.toggle("D7"))
print(s.getTotalTime())
print(s.toggle("D7"))
print(s.toggle("C7"))
print(s.toggle("D7"))
print(s.getTotalTime())
print(s.getMinTime())




# Your BusBooking object will be instantiated and called as such:
# obj = BusBooking(n)
# obj.toggle(seat)
# param_2 = obj.getTotalTime()
# param_3 = obj.getMinTime()