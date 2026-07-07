class Node:
    def __init__(self, key, value, prev, next):
        self.key = key
        self.value = value
        self.prev= prev 
        self.next = next
class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.left = Node(0, 0, None, None)
        self.right = Node(0, 0, None, None)
        self.left.next = self.right
        self.right.prev = self.left
    def insert(self, node):
        prev, next = self.right.prev, self.right
        node.prev = prev
        node.next = next
        self.right.prev = node
        prev.next = node

    def remove(self, node):
        prev, next = node.prev, node.next
        prev.next = next
        next.prev = prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            self.cache[key].value = value
        else:
            if len(self.cache) == self.capacity:
                del self.cache[self.left.next.key]
                self.remove(self.left.next)
                

            self.cache[key] = Node(key, value, None, None)
            self.insert(self.cache[key])

            
