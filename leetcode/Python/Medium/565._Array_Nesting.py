class Solution:
    def arrayNesting(self, nums: list[int]) -> int:
        n = len(nums)
        visit = [False] * n
        ans = 0

        for i in range(n):
            if visit[i]:
                continue

            j = i
            count = 0
            while not visit[j]:
                visit[j] = True
                count+=1

                j = nums[j]

            ans = max(ans, count)

        return ans




s = Solution()
print(s.arrayNesting([5,4,0,3,1,6,2]))