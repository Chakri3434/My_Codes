# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        c1,c2=0,0
        curr = headA
        while curr:
            c1+=1
            curr = curr.next
        curr = headB
        while curr:
            c2+=1
            curr = curr.next
            d=abs(c1-c2)
        if c1>c2:
            curr1 = headA
            for i in range(d):
                curr1 = curr1.next
            curr2 = headB
            while curr1 and curr2:
                if curr1 == curr2:
                    return curr1
                curr1 = curr1.next
                curr2 = curr2.next
            return None
        else:
            curr2 = headB
            for i in range(d):
                curr2 = curr2.next
            curr1 = headA
            while curr1 and curr2:
                if curr1 == curr2:
                    return curr1
                curr1 = curr1.next
                curr2 = curr2.next
            return None
