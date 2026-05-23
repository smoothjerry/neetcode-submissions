"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head
        oldToNew = {}
        while curr:
            new = Node(curr.val)
            oldToNew[curr] = new
            curr = curr.next
        
        curr = head
        while curr:
            new = oldToNew[curr]
            if curr.next:
                new.next = oldToNew[curr.next]
            
            if curr.random:
                new.random = oldToNew[curr.random]
            curr = curr.next

        return oldToNew[head] if head else None