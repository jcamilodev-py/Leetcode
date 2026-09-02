# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        help = []
        prev = head
        current = head.next
        n = 1

        while current.next:
            if current.val > prev.val and current.val > current.next.val or current.val < prev.val and current.val < current.next.val:
                help.append(n)


            current = current.next
            prev = prev.next
            n+=1   


        n = len(help)

        if n >= 2:
            best = float("inf")

            for i in range(1, n):
                best = min(best, help[i] - help[i-1])
    
            return[best, help[-1] - help[0]]

        return [-1,-1]


        





l = ListNode(5)
l.next = ListNode(3)
l.next.next = ListNode(1)
l.next.next.next = ListNode(2)
l.next.next.next.next = ListNode(5)
l.next.next.next.next.next = ListNode(1)
l.next.next.next.next.next.next = ListNode(2)
# l.next.next.next.next.next.next.next = ListNode(10)
# l.next.next.next.next.next.next.next.next = ListNode(6)

s = Solution()
print(s.nodesBetweenCriticalPoints(l))