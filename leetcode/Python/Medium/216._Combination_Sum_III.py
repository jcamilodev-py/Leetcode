class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        ans = []

        def brute_force(i, current, current_sum):
            if len(current) == k:
                if current_sum == n:
                    ans.append(current.copy())
                return

            for i in range(i, 10):
                brute_force(i+1, current + [i], current_sum + i)

        brute_force(1, [], 0)
        return ans



s = Solution()
print(s.combinationSum3(k = 3, n = 7))