from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count, stack, bool, current = 0, [], False, head

        while current.next:
            stack.append(current.val)
            current = current.next
        stack.append(current.val)

        lenn = len(stack)

        while stack:
            if stack[-1]*2 > 9:
                if lenn == 1:
                    bool = True

                value = ((stack[-1] * 2) + count) - 10
                count = 1      
            else:
                value = (stack[-1] * 2) + count
                count = 0
            
            stack.pop()
            lenn-=1

            new_node = ListNode(value)
            new_node.next = current.next
            current.next = new_node

            if bool:
                new_node = ListNode(1)
                new_node.next = current.next
                current.next = new_node

        return current.next


s = Solution()
list1 = ListNode(9)
list1.next = ListNode(9)
list1.next.next = ListNode(9)
print(s.doubleIt(list1))