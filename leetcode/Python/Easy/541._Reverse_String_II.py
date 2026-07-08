class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        
        s = list(s)
        n = len(s)
        st = 0

        while st < n:
            i = st
            j = min(st + k, n) -1
            while i < j:
                s[i], s[j] = s[j], s[i]
                i+=1
                j-=1

            st+= 2*k        
        return "".join(s)


s = Solution()
print(s.reverseStr("hyzqyljrnigxvdtneasepfahmtyhlohwxmkqcdfehybknvdmfrfvtbsovjbdhevlfxpdaovjgunjqlimjkfnqcqnajmebeddqsgl", k = 39))