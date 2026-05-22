# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()
        dummy = ListNode()
        dummy.next = head
        curr = dummy
        while curr:
            if curr.next in seen:
                return True
            
            seen.add(curr)
            curr = curr.next
    
        return False