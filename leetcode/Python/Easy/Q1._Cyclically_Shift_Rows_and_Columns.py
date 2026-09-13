class Solution:
    def cyclicShift(self, n: int, grid: list[list[int]], rowShift: list[int], colShift: list[int]) -> list[list[int]]:

        temp = [[grid[i][(j + rowShift[i]) % n]for j in range(n)] for i in range(n)]

        ans = [[temp[(i + colShift[j]) % n][j] for j in range(n)] for i in range(n)]

        return ans


s = Solution()
print(s.cyclicShift(n = 3, grid = [[1,2,3],[4,5,6],[7,8,9]], rowShift = [1,2,0], colShift = [2,2,1]))