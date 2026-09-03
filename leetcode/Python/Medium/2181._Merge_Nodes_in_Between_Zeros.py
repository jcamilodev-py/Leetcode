from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        ans = ListNode(0)
        current_ans = ans

        count = 0
        s = 0

        while current:
            if current.val == 0:
                count+=1
            else:
                s+=current.val

            if count == 2:
                current_ans.next = ListNode(s)
                current_ans = current_ans.next
                count = 1
                s = 0

            current = current.next

        return ans.next

            

l = ListNode(0)
l.next = ListNode(3)
l.next.next = ListNode(1)
l.next.next.next = ListNode(0)
l.next.next.next.next = ListNode(4)
l.next.next.next.next.next = ListNode(5)
l.next.next.next.next.next.next = ListNode(2)
l.next.next.next.next.next.next.next = ListNode(0)


s = Solution()
print(s.mergeNodes(l))