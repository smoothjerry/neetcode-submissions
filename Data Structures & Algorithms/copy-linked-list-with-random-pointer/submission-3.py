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
        # let's start by copying the list first
        if not head:
            return None
        
        dummy = Node(0)
        oldCurr = head
        prev = None

        queue = deque()
        oldToNew = {}
        while oldCurr:
            newCurr = Node(oldCurr.val)
            oldToNew[oldCurr] = newCurr

            if prev:
                prev.next = newCurr
            else:
                dummy.next = newCurr
            
            if oldCurr.random:
                # newCurr must eventually have random node with this val
                queue.append([newCurr, oldCurr.random])
            prev = newCurr
            oldCurr = oldCurr.next

        # enqueue randoms: map val -> new curr
        while queue:
            node, random = queue.popleft()
            newRandom = oldToNew[random]
            node.random = newRandom
        
        return dummy.next

