import heapq


class Solution:
    def totalCost(self, costs: list[int], k: int, candidates: int) -> int:
        n = len(costs)
        l, r = candidates, n - candidates - 1

        if l > r:
            return sum(sorted(costs)[:k])

        heap1 = [(costs[i], i) for i in range(candidates)]
        heapq.heapify(heap1)

        heap2 = [(costs[i], i) for i in range(n - candidates, n)]
        heapq.heapify(heap2)

        ans = 0
        for _ in range(k):
            if not heap2 or (heap1 and heap1[0] <= heap2[0]):
                i, _j = heapq.heappop(heap1)
                ans += i
                if l <= r:
                    heapq.heappush(heap1, (costs[l], l))
                    l += 1
            else:
                i, _j = heapq.heappop(heap2)
                ans += i
                if l <= r:
                    heapq.heappush(heap2, (costs[r], r))
                    r -= 1
        return ans



        
s = Solution()
print(s.totalCost(costs = [1,2,4,1,2], k = 3, candidates = 3))