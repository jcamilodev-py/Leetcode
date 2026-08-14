class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        dic = {}
        i, j = 0, 0
        n = len(s)
        ans = 1

        while j < n:
            if s[j] not in dic:
                dic[s[j]] = 1
                j+=1
            else:
                if dic[s[j]] >= 2:
                    i+=1
                    j = i
                    dic.clear()
                else:
                    dic[s[j]]+=1
                    j+=1

            ans = max(ans, (j - i))

        return ans





s = Solution()
print(s.maximumLengthSubstring("bcbbbcba"))