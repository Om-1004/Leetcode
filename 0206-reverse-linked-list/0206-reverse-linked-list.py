# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        prev = None
        curr = head
        
        while curr is not None:
            nextNode = curr.next

            curr.next = prev
            prev = curr
            curr = nextNode

        return prev

    
'''
_    1   2   3   4   5
p    c   n

None <-- 1 <-- 2  <-- 3 <-- 4 <--  5   None
                                        c
                                   p   
                                        n





'''
