# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        if (head.next.next == None):
            return head.val+head.next.val
        slow = head
        fast = head
        while(fast!=None):
            slow = slow.next
            fast = fast.next.next
        fast = head
        prev = None
        while(fast!=slow):
            temp = fast.next
            fast.next = prev
            prev = fast
            fast = temp
        ans = 0
        while(prev!=None):
            t = prev.val + slow.val
            if(t>ans):
                ans = t
            prev = prev.next
            slow = slow.next
        return ans