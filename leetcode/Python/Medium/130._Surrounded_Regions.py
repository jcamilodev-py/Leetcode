class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = len(board)
        m = len(board[0])

        def dfs(i, j):
            if i < 0 or j < 0 or i == n or j == m or board[i][j] != "O":
                return
            
            board[i][j] = "A"

            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)

        for i in range(n):
            for j in range(m):
                if board[i][j] == "O" and i in [0, n-1] or j in [0, m-1]:
                    dfs(i,j)

        for i in range(n):
            for j in range(m):
                if board[i][j] == "O":
                    board[i][j] = "X"

        for i in range(n):
            for j in range(m):
                if board[i][j] == "A":
                    board[i][j] = "O"


                        
s = Solution()
print(s.solve([["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]))