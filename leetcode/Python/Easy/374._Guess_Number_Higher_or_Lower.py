# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        # def guess(pick, value):
        #     if value > pick:
        #           return -1
        #     elif value < pick:
        #           return 1
        #     else: return 0

        l = 0
        while l <= n:
            m = (l + n) // 2
            v = guess(6, m)
            if v == -1:
                n = m-1
            elif v == 1:
                l = m+1
            else:
                return m 


s = Solution()
print(s.guessNumber(n = 10))