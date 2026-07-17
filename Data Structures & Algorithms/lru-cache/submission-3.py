class Node:
    def __init__(self, key=0, val=0, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}

        self.lru = Node(0,0)
        self.mru = Node(0,0)

        self.lru.prev, self.lru.next = None, self.mru
        self.mru.prev, self.mru.next = self.lru, None
    
    def remove(self, node):
        prev, next = node.prev, node.next
        prev.next = next
        next.prev = prev

    def insert(self, node):
        prev, next = self.mru.prev, self.mru
        node.prev, node.next = prev, next
        prev.next = node
        next.prev = node
    
    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        node = Node(key, value)
        self.insert(node)
        self.cache[key] = node

        if len(self.cache) > self.cap:
            last = self.lru.next 
            self.remove(last)
            del self.cache[last.key]