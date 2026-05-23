# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find middle, reverse the second half
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # slow is at the middle point.
        # reverse from slow on
        second = slow.next
        prev = slow.next = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        
        # take one node from each until you reach end
        # of second
        first, second = head, prev
        while second:
            tmpSec = second.next
            tmpFirst = first.next
            first.next = second
            second.next = tmpFirst
            first = tmpFirst
            second = tmpSec
