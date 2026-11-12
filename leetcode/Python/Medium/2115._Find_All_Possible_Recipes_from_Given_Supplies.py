from collections import defaultdict, deque

class Solution:
    def findAllRecipes(self, recipes: list[str], ingredients: list[list[str]], supplies: list[str]) -> list[str]:
        adj = defaultdict(list)
        indegree = defaultdict(int)

        for i in range(len(recipes)):
            for j in ingredients[i]:
                adj[j].append(recipes[i])
                indegree[recipes[i]]+=1

        ans = []
        d = deque(supplies)

        while d:
            i = d.pop()

            if i not in adj:
                continue

            for j in adj[i]:
                indegree[j]-=1
                if indegree[j] == 0:
                    ans.append(j)
                    d.append(j)

        return ans


s = Solution()
print(s.findAllRecipes(["bread","sandwich"], ingredients = [["yeast","flour"],["bread","meat"]], supplies = ["yeast","flour","meat"]))