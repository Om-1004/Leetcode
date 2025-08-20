# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        length = 0
        dummyNode = ListNode()
        dummyNode.next = head
        curr = head

 
        
        while curr:
            length += 1
            curr = curr.next


        prev = None
        curr = head
        if length == n:
            return curr.next

        while curr:
            prev = curr
            curr = curr.next
            length -= 1
            if length == n:
                prev.next = curr.next
                return dummyNode.next
            
    

        return None
            
            
            

"""

_ -> 1 -> 2 -> none
          c
     p

length = 1

"""