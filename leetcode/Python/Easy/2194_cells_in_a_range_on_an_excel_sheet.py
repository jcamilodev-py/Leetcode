class Solution:
    def cellsInRange(self, s: str):
        lista = []
        n1 = ord(s[0])
        n2 = ord(s[3])
        start = int(s[1])
        end = int(s[-1])
        for i in range(n1, n2+1):
            for j in range(start, end+1):
                col = chr(i)
                row = str(j)
                output = col+row
                lista.append(output)
        return lista
    
solu = Solution()
print(solu.cellsInRange("K1:L2"))

