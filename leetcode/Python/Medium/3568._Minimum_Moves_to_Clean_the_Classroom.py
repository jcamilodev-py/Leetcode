from typing import List
from collections import deque

class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])

        start = None
        litter_positions = []
        for r in range(m):
            for c in range(n):
                if classroom[r][c] == 'S':
                    start = (r, c)
                elif classroom[r][c] == 'L':
                    litter_positions.append((r, c))
        
        litter_index = {pos: i for i, pos in enumerate(litter_positions)}
        full_mask = (1 << len(litter_positions)) - 1
        
        if full_mask == 0:
            return 0  
        
        sr, sc = start
        start_mask = 0
        
        visited = set()
        start_state = (sr, sc, energy, start_mask)
        visited.add(start_state)
        queue = deque([(sr, sc, energy, start_mask, 0)])
        
        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        
        while queue:
            r, c, e, mask, steps = queue.popleft()
            
            if e == 0:
                continue 
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if not (0 <= nr < m and 0 <= nc < n):
                    continue
                if classroom[nr][nc] == 'X':
                    continue
                
                new_e = e - 1
                if classroom[nr][nc] == 'R':
                    new_e = energy 
                
                new_mask = mask
                if (nr, nc) in litter_index:
                    new_mask |= (1 << litter_index[(nr, nc)])
                
                state = (nr, nc, new_e, new_mask)
                if state in visited:
                    continue
                
                if new_mask == full_mask:
                    return steps + 1
                
                visited.add(state)
                queue.append((nr, nc, new_e, new_mask, steps + 1))
        
        return -1




s = Solution()
print(s.minMoves(["S.", "XL"], energy = 2))