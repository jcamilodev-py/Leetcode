class Solution:
    def minInsertions(self, s: str) -> int:
        depth = 0
        ans = 0

        for i in s:
            if i == "(":
                depth+=2
                if depth % 2 != 0:
                    depth-=1
                    ans+=1
            else:
                depth-=1

                if depth < 0:
                    ans+=1
                    depth = 1

        return ans + depth





s = Solution()
print(s.minInsertions("(()))(()))()())))"))