# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if(head==None):
            return head
        if(head.next==None):
            head = None
            return head
        l = 0
        curr = head
        while(curr!=None):
            l += 1
            curr = curr.next
        m = (l//2)+1
        prev = head
        for c in range(m-2):
            prev = prev.next
        mid = prev.next
        prev.next = mid.next
        return head