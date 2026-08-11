from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        current1, current2 = l1, l2
        n1, n2 = [], []
        while current1:
            n1.append(str(current1.val))
            current1 = current1.next

        while current2:
            n2.append(str(current2.val))
            current2 = current2.next

        n1 = n1[::-1]
        n2 = n2[::-1]

        n1 = int("".join(n1))
        n2 = int("".join(n2))

        number = str(n1 + n2)
        ans = ListNode(0)
        current = ans
        for i in reversed(number):
            current.next = ListNode(int(i))
            current = current.next

        return ans.next



l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

s = Solution()
print(s.addTwoNumbers(l1, l2))