class Node:
    def __init__(self, key, value, prev, next):
        self.key = key
        self.val = value
        self.prev = prev
        self.next = next
class LRUCache:

    def __init__(self, capacity: int):
        self.map = {}
        self.left = Node(0,0, None, None)
        self.right = Node(0,0, None, None)
        self.left.next = self.right
        self.right.prev = self.left
        self.cap = capacity
    
    def remove(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev
    
    def insert(self, node):
        #insert into left
        next = self.left.next
        next.prev = node
        self.left.next = node
        node.prev = self.left
        node.next = next
        

    def get(self, key: int) -> int:
        if key in self.map:
            node = self.map[key]
            self.remove(node)
            self.insert(node)
            return node.val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.map[key].val = value
            self.remove(self.map[key])
            self.insert(self.map[key])
        else:
            node = Node(key, value, None, None)
            if len(self.map) == self.cap:
                lru = self.right.prev
                self.remove(lru)
                del self.map[lru.key]
            self.insert(node)
            self.map[key] = node

        
