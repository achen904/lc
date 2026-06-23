# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        head = lists[0]
        def merge2(l1, l2):
            dummy = node = ListNode(0)
            while l1 and l2:
                if l1.val < l2.val:
                    node.next = l1
                    l1 = l1.next
                else:
                    node.next = l2
                    l2 = l2.next
                node = node.next
            if l1:
                node.next = l1
            elif l2:
                node.next = l2
            return dummy.next
        for i in range(1, len(lists)):
            head = merge2(head, lists[i])
        return head