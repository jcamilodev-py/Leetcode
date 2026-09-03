from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:

        ans = [[-1] * n for _ in range(m)]

        t, b, l, r = 0, m - 1, 0, n - 1

        current = head

        while current and t <= b and l <= r:


            for i in range(l, r+1):
                if not current:
                    break
                ans[t][i] = current.val
                current = current.next

            t+=1

            for i in range(t, b+1):
                if not current:
                    break
                ans[i][r] = current.val
                current = current.next

            r-=1

            if t <= b:
                for i in range(r, l-1, -1):
                    if not current:
                        break

                    ans[b][i] = current.val
                    current = current.next

                b-=1

            if l <= r:
                for i in range(b, t-1, -1):
                    if not current:
                        break

                    ans[i][l] = current.val
                    current = current.next

                l+=1

        return ans



l = ListNode(3)
l.next = ListNode(0)
l.next.next = ListNode(2)
l.next.next.next = ListNode(6)
l.next.next.next.next = ListNode(8)
l.next.next.next.next.next = ListNode(1)
l.next.next.next.next.next.next = ListNode(7)
l.next.next.next.next.next.next.next = ListNode(9)
l.next.next.next.next.next.next.next.next = ListNode(4)
l.next.next.next.next.next.next.next.next.next = ListNode(2)
l.next.next.next.next.next.next.next.next.next.next = ListNode(5)
l.next.next.next.next.next.next.next.next.next.next.next = ListNode(5)
l.next.next.next.next.next.next.next.next.next.next.next.next = ListNode(0)

s = Solution()
print(s.spiralMatrix(3, 5, l))