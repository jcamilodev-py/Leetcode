class Solution:
    def findColoredRoot(self, edges: list[list[int]], colors: str) -> int:
        n = len(colors)
        next = {'R': 'B', 'B': 'W', 'W': 'R'}
        parents = [0] * n

        childs = [0] * n

        for u, v in edges:
            if next[colors[u]] == colors[v]:
                parent, child = u, v

            elif next[colors[v]] == colors[u]:
                parent, child = v, u

            else:
                return -1

            parents[child]+=1
            childs[parent]+=1

            if parents[child] > 1 or childs[parent] > 2:
                return -1

        for i in range(n):
            if parents[i] == 0:
                return i

        return -1
        
            


        

s = Solution()
print(s.findColoredRoot([[3,1],[3,2],[1,4],[2,0]], colors = "BRRWB"))