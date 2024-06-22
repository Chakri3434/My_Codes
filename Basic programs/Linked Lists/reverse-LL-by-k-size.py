# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head
        size=0
        while curr:
            size+=1
            curr = curr.next
        def reverse(head,k,size):
            curr = head
            prev = None
            nxt = None
            if size<k:
                return curr
            c=0
            while curr and c<k:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
                c+=1
            size-=c
            if nxt:
                newHead = reverse(nxt,k,size)
                head.next = newHead
            return prev
        return reverse(head,k,size)
