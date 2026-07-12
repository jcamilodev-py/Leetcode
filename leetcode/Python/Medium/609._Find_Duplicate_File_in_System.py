from collections import defaultdict
from typing import List

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        l = defaultdict(list)

        for i in paths:
            inputs = i.split()

            d, f = inputs[0], inputs[1:]

            for j in f:
                fname, content = j.split("(")
                content = content[:-1]

                l[content].append(f"{d}/{fname}")

        ans = []
        for k in l.values():
            if len(k) > 1:
                ans.append(k)
        return ans



s = Solution()
print(s.findDuplicate(["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)","root 4.txt(efgh)"]))