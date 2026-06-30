from typing import Counter

class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        count = Counter(target)
        seen = set(target)
        seens = set(s)
        dic = {}
        for i in s:
            if i in seen and i in dic:
                dic[i]+=1
            elif i in seen:
                dic[i] = 1

        for i in count:
            if i in seens:
                dic[i] //= count[i]
            else:
                return 0
        
        return min(dic.values())


s = Solution()
print(s.rearrangeCharacters("abc", target = "abcd"))