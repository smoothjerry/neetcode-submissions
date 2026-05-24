class Node:

    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity
        self.left = Node(0,0)
        self.right = Node(0,0)
        self.left.nxt = self.right
        self.right.prev = self.left
    
    def remove(self, node):
        """
        remove from the dll
        """
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev
    
    def insert(self, node):
        """
        put at the MRU spot
        """
        prev = self.right.prev
        prev.next = node
        node.prev = prev
        node.next = self.right
        self.right.prev = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        # moves node to MRU spot
        self.remove(self.cache[key])
        self.insert(self.cache[key])
        
        # return the value
        return self.cache[key].val
        

    def put(self, key: int, value: int) -> None:
        # remove from dll -- accessing now
        if key in self.cache:
            self.remove(self.cache[key])
        
        node = Node(key, value)
        self.cache[key] = node
        self.insert(node)

        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

        
        # TODO: put in list as MRU

        # TODO: invalidate LRU if cache too large
        
