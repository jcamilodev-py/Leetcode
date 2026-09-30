import heapq

class SmallestInfiniteSet:

    def __init__(self):
        self.heap = []
        self.used = set({1})
        self.last = 1

        heapq.heapify(self.heap)
        heapq.heappush(self.heap, 1)
        
        

    def popSmallest(self) -> int:
        v = heapq.heappop(self.heap)
        self.used.remove(v)
        self.last+=1

        self.addBack(self.last)

        return v


    def addBack(self, num: int) -> None:
        if num not in self.used:
            heapq.heappush(self.heap, num)
            self.used.add(num)

        
        

s = SmallestInfiniteSet()
print(s.addBack(2))
print(s.popSmallest())
print(s.popSmallest())
print(s.popSmallest())
print(s.addBack(1))
print(s.popSmallest())
print(s.popSmallest())
print(s.popSmallest())



# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)