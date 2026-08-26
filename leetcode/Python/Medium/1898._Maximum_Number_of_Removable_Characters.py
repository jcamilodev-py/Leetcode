from typing import List

class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        n = len(s)
        m = len(p)

        def is_correct(k):
            seen = set(removable[:k])
            j = 0
            for i in range(n):
                
                if i not in seen:
                    if s[i] == p[j]:
                        j+=1

                if j == m:
                    return True 
            return False
                
        l, r = 0, len(removable)
        ans = 0
        while l <= r:
            mid = ((l + r) // 2)

            if is_correct(mid):
                ans = mid
                l = mid + 1
            else:
                r = mid - 1

        return ans



s = Solution()
print(s.maximumRemovals(s = "abcacb", p = "ab", removable = [3,1,0]))