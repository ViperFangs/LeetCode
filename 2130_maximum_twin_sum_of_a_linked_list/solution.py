# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = fast = head
        slow_tail = None
        max_sum = 0

        while fast and fast.next:
            fast = fast.next.next
            temp_node = slow.next
            slow.next = slow_tail
            slow_tail = slow
            slow = temp_node
        
        while slow and slow_tail:
            max_sum = max(slow.val + slow_tail.val, max_sum)
            slow = slow.next
            slow_tail = slow_tail.next
        return max_sum