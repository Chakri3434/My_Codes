# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

## NAIVE SOLUTION ##
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        call = root = ListNode(0)
        s=[]
        curr = head
        while curr:
            s.append(curr.val)
            curr = curr.next
        s=s[::-1]
        print(s[::-1])
        if not s:
            return
        for i in range(len(s)):
            root.next = ListNode(s[i])
            root = root.next
        return call.next

## EFFICIENT-ITERATIVE ##
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        curr = head
        prev = None
        while curr:
            nextt = curr.next
            curr.next = prev
            prev = curr
            curr = nextt
        return prev
## RECURSIVE ##
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        newHead = head
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head
        head.next = None
        return newHead
