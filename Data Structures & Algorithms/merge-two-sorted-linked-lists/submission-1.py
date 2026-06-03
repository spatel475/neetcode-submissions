# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def print_listnode(self, head):
        current = head
        result = []

        while current:
            result.append(str(current.val))
            current = current.next

        print(" -> ".join(result))

    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:

        if list1 is None and list2 is None:
            return None

        if list1 is None:
            return list2

        if list2 is None:
            return list1

        dummy = ListNode(0)
        curr = dummy

        # self.print_listnode(curr)

        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                curr.next = ListNode(list1.val, list1.next)
                curr = curr.next
                list1 = list1.next
            else:
                curr.next = ListNode(list2.val, list2.next)
                curr = curr.next
                list2 = list2.next
            # self.print_listnode(curr)

        if list1 is not None and list2 is None:
            curr.next = list1
        elif list1 is None and list2 is not None:
            curr.next = list2

        return dummy.next
