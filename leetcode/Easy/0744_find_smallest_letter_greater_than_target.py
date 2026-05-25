from typing import List

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        order_letters = sorted(letters)

        for i in order_letters:
            if ord(i) > ord(target):
                return i
        return letters[0]


s = Solution()
print(s.nextGreatestLetter(["c","f","j"], target = "c"))