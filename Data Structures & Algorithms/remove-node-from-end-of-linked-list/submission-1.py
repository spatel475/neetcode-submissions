# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head

        fast, slow = dummy.next, dummy

        counter = 1

        while fast.next:
            print(counter, fast.val)
            fast = fast.next
            counter += 1

            if counter > n and slow:
                # print("slow now at", slow.val)
                slow = slow.next

        # edge case - if counter didn't increment,
        # there must be only 1 node in list
        # so return empty list after deleting only node
        if counter == 1:
            return None

        if slow.next:
            # print("updating slow to", slow.next.next.val)
            slow.next = slow.next.next

        return dummy.next
