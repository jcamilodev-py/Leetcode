from typing import List

class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        dic = {p[0]:i for i,p in enumerate(pieces)}

        tmp = []

        for i in arr:
            if i in dic:
                tmp.extend(pieces[dic[i]])
        
        return tmp == arr




s = Solution()
print(s.canFormArray([91,4,64,78], pieces = [[78],[4,64],[91]]))