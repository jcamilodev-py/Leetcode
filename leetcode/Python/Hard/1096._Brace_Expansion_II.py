class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:

        def build(s):
            p = set()

            current = {""}
            i = 0

            while i < len(s):
                if s[i] == "{":
                    j = i
                    depth = 0

                    while True:
                        if s[j] == "{":
                            depth-=1
                        elif s[j] == "}":
                            depth+=1
                        if depth == 0:
                            break
                        j+=1
                    options = build(s[i+1:j])
                    current = {a + b for a in current for b in options}
                    i = j + 1

                elif s[i] == ",":
                    p |= current
                    current = {""}
                    i+=1
                else:
                    current = {x + s[i] for x in current}
                    i+=1

            p|=current

            return p

        return sorted(build(expression))




s = Solution()
print(s.braceExpansionII(expression = "{a,b}{c,{d,e}}"))