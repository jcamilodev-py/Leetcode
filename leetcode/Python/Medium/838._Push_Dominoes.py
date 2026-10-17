class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        ans = []

        i, j = 0, 1
        dominoes = list(dominoes)

        dominoes.insert(0, "L")
        dominoes.append("R")

        n = len(dominoes)

        while j < n:
            if dominoes[i] != ".":
                while j < n and dominoes[j] == ".":
                    j+=1

                if dominoes[i] == "L" and dominoes[j] == "R":
                    ans.append("." * (j-1-i))

                elif dominoes[i] == "L" and dominoes[j] == "L":
                    ans.append("L" * (j-1-i))

                elif dominoes[i] == "R" and dominoes[j] == "L":
                    m = j-1-i

                    r = "R" * (m // 2)
                    p = "." * ((j-1-i) % 2)
                    l = "L" * (m // 2)

                    ans.append(r + p + l)
                else:
                    ans.append("R" * (j-1-i))
                    
                ans.append(dominoes[j])

                i = j

            else:
                i+=1

            if i == j:
                j+=1

        ans.pop()
        return "".join(ans)





s = Solution()
print(s.pushDominoes(dominoes = ".L.R...LR..L.."))