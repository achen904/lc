class Node:
    def __init__(self, value, key, next, prev):
        self.val = value
        self.key = key
        self.next = next
        self.prev = prev
class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.l = Node(0,0, None, None)
        self.r = Node(0,0, None, None)
        self.l.next = self.r
        self.r.prev = self.l
    #create a helper to easily remove a node from the list
    def remove(self, node):
        #1 <--> 2 <--> 3
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev
    #Create a helper to easily enter a node at front 
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
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            node.val = value
            self.insert(node)
            self.cache[key] = node
        else:
            node = Node(value, key, None, None)
            if len(self.cache) == self.capacity:
                lru = self.l.next
                del self.cache[lru.key]
                self.remove(lru)
            self.insert(node)
            self.cache[key] = node
