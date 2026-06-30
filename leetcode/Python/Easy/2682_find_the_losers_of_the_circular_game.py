class Solution:
    def circularGameLosers(self, n: int, k: int):
        visitados = [0] * n   
        pos = 0               
        paso = 1              

        while visitados[pos] == 0:
            visitados[pos] += 1
            pos = (pos + paso * k) % n
            paso += 1

        return [i + 1 for i in range(n) if visitados[i] == 0]
            
            
            

s = Solution()
print(s.circularGameLosers(n = 5, k = 2))