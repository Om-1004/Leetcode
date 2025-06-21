# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = list1
        curr2 = list2

        dummy = ListNode()
        mover = dummy


        while curr1 is not None and curr2 is not None:
            top = curr1.val
            bottom = curr2.val

            if top >= bottom:
                mover.next = curr2
                curr2 = curr2.next
            else:
                mover.next = curr1
                curr1 = curr1.next

            mover = mover.next

        if curr1 is None:
            mover.next = curr2

        if curr2 is None:
            mover.next = curr1

        return dummy.next

'''

___ --> 1 --> 1 --> 2 --> 3 --> 4
                                m


1 --> 2 --> 4 --> None
            _
 
1 --> 3 --> 4 --> None
                    _


'''