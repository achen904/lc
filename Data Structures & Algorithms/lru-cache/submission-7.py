class Node:
    def __init__(self, key, value, next, prev):
        self.key = key
        self.val = value
        self.next = next
        self.prev = prev
class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity
        self.l = Node(0,0, None, None)
        self.r = Node(0, 0, None, None)
        self.l.next = self.r
        self.r.prev = self.l
    
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev
    def insert(self, node):
        prev = self.r.prev
        prev.next = node
        node.prev = prev
        node.next = self.r
        self.r.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            node.val = value
            self.insert(node)
            self.cache[key] = node
        else:
            if len(self.cache) == self.cap:
                lru = self.l.next
                self.remove(lru)
                del self.cache[lru.key]
            node = Node(key, value, None, None)
            self.insert(node)
            self.cache[key] = node        
