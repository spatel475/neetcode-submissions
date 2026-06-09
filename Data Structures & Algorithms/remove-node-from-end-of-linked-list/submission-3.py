# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left, right = dummy, dummy.next
        counter = 1

        while right.next:
            right = right.next
            counter += 1

            if counter > n and left:
                left = left.next

        # if counter didn't increment, there must be 1 node in list, so return empty list after deleting only node
        if counter == 1:
            return None

        left.next = left.next.next
        return dummy.next
