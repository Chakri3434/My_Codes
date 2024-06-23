# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = pre = ListNode(0)
        dummy.next = head
        while head and head.next:
            if head.val == head.next.val:
                while head and head.next and head.val == head.next.val:
                    head = head.next
                head = head.next
                pre.next = head
            else:
                pre = pre.next
                head = head.next
        return dummy.next


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        d={}
        curr = head
        while curr:
            if curr.val in d:
                d[curr.val]+=1
            else:
                d[curr.val]=1
            curr = curr.next
        s=set()
        for k,v in d.items():
            if v>1:
                s.add(k)
        print(s)
        dummy = pre = ListNode(0)
        dummy.next = head
        while dummy and dummy.next:
            if dummy.next.val in s:
                dummy.next = dummy.next.next
            else:
                dummy = dummy.next
        return pre.next
        
