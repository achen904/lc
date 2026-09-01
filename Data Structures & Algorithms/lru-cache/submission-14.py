#since we want to update the cache in O(1), we need to be able to access items in the middle of the cache in O(1) and put them at the beginning of the cache
#if the cache gets full then we need to be able to look at the LRU item and remove it
#to do this we can use a dictionary to store nodes corresponding to their key so that we can get it in O(1) then we need to put at the beginnign of the cache
#also if we put an item at then we need to insert it at the beginning cache and if the cache is full remove the item at the end of the cache
#to be able to remove elements in the middle of the cache and track the LRU we can use a doubly linked list where we have a right pointer that poitns to the LRU and a left pointer to point to the MRU beginning, the doubly linnked list also allows us to remove items and update the items next to them
class Node:
    def __init__(self, key, val, next, prev):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev
class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity
        self.left = Node(0,0,None, None)
        self.right = Node(0,0, None, None)
        #point the left and right pointers to each is the cache is empty
        self.left.next = self.right
        self.right.prev = self.left
    def insert(self, node):
        #we only insert at the beginning
        nxt = self.left.next
        node.next = nxt
        self.left.next = node
        node.prev = self.left
        nxt.prev = node
    def remove(self, node):
        nxt = node.next
        prv = node.prev
        prv.next =nxt
        nxt.prev = prv

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
            self.cache[key].val = value
            self.insert(self.cache[key])
        else:
            node = Node(key, value, None, None)
            self.insert(node)
            if len(self.cache) == self.cap:
                lru = self.right.prev
                del self.cache[lru.key]
                self.remove(lru)
            self.cache[key] = node