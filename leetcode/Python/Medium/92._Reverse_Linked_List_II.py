from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        current = head
        count = 1
        prev = None

        while current != None:
            if count >= left and count <= right:
                if count == left:
                    start = current
                
                if count == right:
                    after = current.next

                next_node = current.next
                current.next = prev
                prev = current
                current = next_node

            else:
                if count == left-1:
                    before = current
                current = current.next
            count+=1


        
        start.next = after
        
        if left == 1:
            return prev
        else:
            before.next = prev
            return head


s = Solution()
list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(3)
list1.next.next.next = ListNode(4)
list1.next.next.next.next = ListNode(5)

print(s.reverseBetween(list1, 2, 4))
