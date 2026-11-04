class Solution:
    def longestCycle(self, edges: list[int]) -> int:
        n = len(edges)
        ans = -1

        visit = [False] * n

        for i in range(n):
            if visit[i]:
                continue
            dic = {}
            count = 1
            j = i

            while j != -1 and not visit[j]:
                visit[j] = True
                dic[j] = count
                count+=1

                j = edges[j]
            if j in dic:
                ans = max(ans, (count - dic[j]))

        return ans


s = Solution()
print(s.longestCycle([2,-1,3,1]))