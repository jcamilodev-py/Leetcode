from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        i = 0
        write = 0

        while i < n:
            current_char = chars[i]
            count = 0

            while i < n and chars[i] == current_char:
                i += 1
                count += 1

      
            chars[write] = current_char
            write += 1

            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write+=1
        return write



s = Solution()
print(s.compress(["a","a","b","b","c","c","c"]))