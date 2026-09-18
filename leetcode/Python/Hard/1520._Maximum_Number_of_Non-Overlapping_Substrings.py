from collections import Counter


class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        f, l = {}, {}
        for i, j in enumerate(s):
            if j not in f:
                f[j] = i
            l[j] = i

        def expand(i):

            r = l[s[i]]
            k = i
            while k <= r:
                if f[s[k]] < i: 
                    return -1
                r = max(r, l[s[k]])
                k += 1
            return r

        ans = []
        prev_r = -1
        for i, j in enumerate(s):
            if i != f[j]:
                continue
            r = expand(i)
            if r == -1:
                continue
            if i > prev_r:         
                ans.append(s[i:r + 1])
            else:                    
                ans[-1] = s[i:r + 1]
            prev_r = r

        return ans

       

s = Solution()
print(s.maxNumOfSubstrings("adefaddaccca"))