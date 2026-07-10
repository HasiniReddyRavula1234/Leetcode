# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev, curr, node = None, head, head
        count, c = 0, 0
        while node:
            c += 1
            node = node.next
        pos = c - n + 1
        if pos == 1:
            return head.next
        while curr:
            count += 1
            if count == pos:
                prev.next = curr.next
                break
            prev = curr
            curr = curr.next
        return head
            