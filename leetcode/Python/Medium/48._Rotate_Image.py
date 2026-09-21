from copy import deepcopy

class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        m = deepcopy(matrix)
        n = len(matrix)

        x, y = 0, n-1

        for i in range(n):
            for j in range(n):
                matrix[x][y] = m[i][j]
                x+=1

            x = 0
            y-=1



s = Solution()
print(s.rotate([[1,2,3],[4,5,6],[7,8,9]]))