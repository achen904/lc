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
        map = {None: None}
        cur = head
        while cur:
            copy= Node(cur.val)
            map[cur] = copy
            cur = cur.next
        cur = head
        while cur:
            copy = map[cur]
            copy.next = map[cur.next]
            copy.random = map[cur.random]
            cur = cur.next
        return map[head]