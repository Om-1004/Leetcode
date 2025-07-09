# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummyMover = dummy

        curr1 = l1
        curr2 = l2
        
        carry = 0

        while curr1 is not None or curr2 is not None:
            nodeVal = None
            if curr1 and curr2:
                val1 = curr1.val
                val2 = curr2.val
                nodeVal = (val1 + val2 + carry)
                curr1 = curr1.next
                curr2 = curr2.next
            
            elif curr1 is not None:
                val1 = curr1.val
                nodeVal = val1 + carry
                curr1 = curr1.next

            else:
                val2 = curr2.val
                nodeVal = val2 + carry
                curr2 = curr2.next


            if nodeVal // 10 >= 1:
                carry = nodeVal // 10
            else:
                carry = 0
            
            newNode = ListNode(nodeVal % 10)
            dummyMover.next = newNode
            dummyMover = dummyMover.next

        if carry:
            dummyMover.next = ListNode(1)
        return dummy.next
