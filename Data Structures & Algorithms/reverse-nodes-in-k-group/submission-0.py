# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def getKth(cur, k):
            while cur and k > 0:
                cur = cur.next
                k -= 1
            return cur
        dummy = ListNode(0, head)
        GroupPrev = dummy
        while True:
            kth = getKth(GroupPrev, k)
            if not kth:
                break
            GroupNext = kth.next
            prev = kth.next
            curr = GroupPrev.next
            while curr != GroupNext:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            tmp = GroupPrev.next
            GroupPrev.next = kth
            GroupPrev = tmp
        return dummy.next