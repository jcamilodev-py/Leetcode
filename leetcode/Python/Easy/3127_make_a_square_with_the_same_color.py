class Solution:
    def canMakeSquare(self, grid):
        for i in range(2):
            for j in range(2):
                B = 0
                W = 0
                for x in range(i, i + 2):
                    for y in range(j, j + 2):
                        if grid[x][y] == "B":
                            B += 1
                        else:
                            W += 1
                if max(B, W) >= 3:
                    return True

        return False



s = Solution()
print(s.canMakeSquare([["B","W","B"],["W","B","B"],["B","B","B"]]))