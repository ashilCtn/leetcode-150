# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        slow.next = None
        prev = None
        
        while second:
            next = second.next
            second.next = prev
            prev = second
            second = next

        first = head
        while prev:
            t1, t2 = first.next, prev.next
            first.next = prev
            prev.next = t1
            first = t1
            prev = t2

