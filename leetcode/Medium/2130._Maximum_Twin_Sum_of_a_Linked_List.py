from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        if not head or not head.next:
            return head

        slow = head
        fast = head.next
        l = []
        ans = float('-inf')

        while fast and fast.next:
            l.append(slow.val)
            slow = slow.next
            fast = fast.next.next
        l.append(slow.val)
        slow = slow.next

        while slow:
            item = l.pop()
            ans = max(ans, slow.val + item)
            
            slow = slow.next
        
        return ans


s = Solution()
list1 = ListNode(4)
list1.next = ListNode(2)
list1.next.next = ListNode(2)
list1.next.next.next = ListNode(3)

print(s.pairSum(list1))