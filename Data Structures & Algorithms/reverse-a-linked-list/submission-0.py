# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        h = head
        prev = None

        while h:
            curr = h
            nxt = curr.next
            curr.next = prev
            prev = curr
            h = nxt

        return prev
