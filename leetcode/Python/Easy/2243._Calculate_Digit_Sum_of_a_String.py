class Solution:
    def digitSum(self, s: str, k: int) -> str:

        def h(c, s):
            count = 0
            value = 0
            for i in s:
                value+=int(i)
                count+=1

                if count == k:
                    c.append(str(value))
                    count = 0
                    value = 0

            if count > 0:
                c.append(str(value))

            return "".join(c)

        while len(s) > k:
            s = h([], s)
        
        return s


s = Solution()
print(s.digitSum(s = "11111222223", k = 3))