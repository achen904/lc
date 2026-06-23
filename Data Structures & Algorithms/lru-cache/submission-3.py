class Node:
        def __init__(self, key, value, next, prev):
            self.val = value
            self.next = next
            self.prev = prev
            self.key = key
class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.left = Node(0, 0, None, None)
        self.right = Node(0, 0, None, None)
        self.left.next = self.right
        self.right.prev = self.left
    
    def insert(self, node):
        prev, next = self.right.prev, self.right
        node.next = next
        node.prev = prev
        prev.next = node
        next.prev = node
    def remove(self, node):
        prev, next = node.prev, node.next
        prev.next = next
        next.prev = prev


    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            self.cache[key].val = value
        else:
            self.cache[key] = Node(key, value, None, None)
            self.insert(self.cache[key])
        if len(self.cache) > self.cap:
            del self.cache[self.left.next.key]
            self.remove(self.left.next)
        
