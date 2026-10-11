class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits: return []
        dic = {
            "2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"
        }

        ans = []
        def brute_force(i, current):
            if len(current) == len(digits):
                ans.append(current)
                return

            for c in dic[digits[i]]:
                brute_force(i+1, current + c)

        brute_force(0, "")

        return ans 



s = Solution()
print(s.letterCombinations("239"))