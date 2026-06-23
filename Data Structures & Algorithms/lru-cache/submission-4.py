class Node:
    def __init__(self, value, key, next, prev):
        self.value = value
        self.next = next
        self.prev = prev
        self.key = key
#We want to use a doubly linked list so that we can easily
#insert and remove elements from the cache        
class LRUCache:

    def __init__(self, capacity: int):
        self.size = capacity
        self.cache = {} 
        self.l = Node(0, 0, None, None)
        self.r = Node(0, 0, None, None)
        self.l.next = self.r
        self.r.prev = self.l
    def remove(self, node):
        next = node.next
        prev = node.prev
        prev.next = next
        next.prev = prev
    def insert(self, node):
        #add to front only self.r used
        nxt = self.r
        prev = self.r.prev
        prev.next = node
        node.prev = prev
        nxt.prev = node
        node.next = nxt
        
    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            node = Node(value, key, None, None)
            if len(self.cache) == self.size:
                del self.cache[self.l.next.key]
                self.remove(self.l.next)
            self.cache[key] = node
            self.insert(node)
        if key in self.cache:
            node = self.cache[key]
            self.cache[key].val = value
            self.remove(node)
            self.insert(node)    
        
