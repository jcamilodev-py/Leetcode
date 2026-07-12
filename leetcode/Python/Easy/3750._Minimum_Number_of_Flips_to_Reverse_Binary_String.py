class Solution:
    def minimumFlips(self, n: int) -> int:
        n = str(bin(n))
        ans = 0

        i,j = 2, len(n)-1
        while i < j:
            if n[i] != n[j]:
                ans+=2
            i+=1
            j-=1
        return ans

s = Solution()
print(s.minimumFlips(10))