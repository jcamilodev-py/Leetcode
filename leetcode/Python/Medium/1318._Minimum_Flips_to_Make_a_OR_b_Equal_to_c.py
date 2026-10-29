class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        ans = 0

        while a > 0 or b > 0 or c > 0:
            ab = a & 1
            bb = b & 1
            cb = c & 1

            if cb == 1:
                if (ab | bb) != 1:
                    ans+=1
            else:
                if ab == 1:
                    ans+=1
                if bb == 1:
                    ans+=1

            a >>= 1
            b >>= 1
            c >>= 1
        return ans



s = Solution()
print(s.minFlips(a = 8, b = 3, c = 5))