class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        n = len(s)

        b = []
        i = 0
        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1
            b.append((s[i], j - i, i, j - 1))
            i = j
    
        total = s.count('1')
    
        maximum = 0
        for t, tam, i, f in b:
            if t == '0':
                maximum = max(maximum, tam)
    
        best = 0
    
        for idx in range(len(b)):
            t, m, i, f = b[idx]
        
            if t != '1':
                continue
        
            l = idx - 1 >= 0 and b[idx - 1][0] == '0'
            r = idx + 1 < len(b) and b[idx + 1][0] == '0'
        
            if not (l and r):
                continue
        
            L = b[idx - 1][1]
            R = b[idx + 1][1]
        
            local = L + R
            ex = maximum - m
        
            best = max(best, local, ex)
    
        return total + best



s = Solution()
print(s.maxActiveSectionsAfterTrade("01"))