class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        ans = []
        dic = {}

        for i,j in knowledge:
            dic[i] = j
        i = 0
        v = False
        for j in range(len(s)):
            if s[j] == "(":
                v = True
                i = j
            elif s[j] == ")":
                v = False
                if s[i+1:j] in dic:
                    ans.append(dic[s[i+1:j]])
                else:
                    ans.append("?")
            elif v == False:
                ans.append(s[j])

        return "".join(ans)

            



s = Solution()
print(s.evaluate(s = "hi(name)", knowledge = [["a","b"]]))