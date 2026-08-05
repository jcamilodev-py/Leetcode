from typing import List
import heapq

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        nums.sort()
        n = len(nums)
        self.nums = nums[n - k:] if n - k > 0 else nums[0:]
        heapq.heapify(nums)


    def add(self, val: int) -> int:
        if len(self.nums) == self.k:
            v = self.nums[0]
            heapq.heappushpop(self.nums, max(v, val))
        else:
            heapq.heappush(self.nums, val)

        return self.nums[0]




# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

s = KthLargest(3, [5, -1])

print(s.add(2))
print(s.add(1))
print(s.add(-1))
print(s.add(3))
print(s.add(4))


