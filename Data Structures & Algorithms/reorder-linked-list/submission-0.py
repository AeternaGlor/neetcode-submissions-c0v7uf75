# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # split
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        # if not slow.next:
        #     return
        mid = slow.next
        slow.next = None
        
        # reverse second half
        curr = mid
        prev = None
        while curr:
            following = curr.next
            curr.next = prev
            prev = curr
            curr = following
        
        # merge
        while head and prev:
            following1 = head.next
            following2 = prev.next

            head.next = prev
            head = following1
            
            prev.next = following1
            prev = following2