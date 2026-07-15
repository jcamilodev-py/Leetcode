from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(board)
        m = len(board[0])
        seen = set()
        def dfs(char_idx, i, j):
            if i < 0 or i >= n or j < 0 or j >= m:
                return
            
            if board[i][j] != word[char_idx] or (i,j) in seen:
                return
            
            seen.add((i,j))

            if char_idx == len(word)-1:
                return True
            
            df = dfs(char_idx+1, i+1, j)or dfs(char_idx+1, i-1, j) or dfs(char_idx+1, i, j+1) or dfs(char_idx+1, i, j-1)
            seen.remove((i,j))

            return df
        


        for i in range(n):
            for j in range(m):
                if dfs(0, i, j):
                    return True
        return False


            
s = Solution()
print(s.exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"))