import heapq


class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        available = [[w, s] for s, w in enumerate(servers)]
        heapq.heapify(available)
        using = []
        n = len(tasks)

        res = []
        for i in range(n):
            while using and using[0][0] <= i:
                et, w, s = heapq.heappop(using)
                heapq.heappush(available, [w, s])
            if available:
                w, s = heapq.heappop(available)
                heapq.heappush(using, [i + tasks[i], w, s])
            else:
                et, w, s = heapq.heappop(using)
                heapq.heappush(using, [et + tasks[i], w, s])
            res.append(s)
        return res



s = Solution()
print(s.assignTasks(servers = [3,3,2], tasks = [1,2,3,2,1,2]))