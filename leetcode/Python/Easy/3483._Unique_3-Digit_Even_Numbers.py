from typing import List

class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        n = len(digits)
        used = [False] * n
        res = set()

        def recursion(num, length):
            if length == 3:
                if num % 2 == 0:
                    res.add(num)
                return

            for i in range(n):
                if used[i]:
                    continue
                if length == 0 and digits[i] == 0:
                    continue

                used[i] = True
                recursion(num * 10 + digits[i], length + 1)
                used[i] = False

        recursion(0, 0)
        return len(res)

                    


s = Solution()
print(s.totalNumbers([1,2,3,4]))