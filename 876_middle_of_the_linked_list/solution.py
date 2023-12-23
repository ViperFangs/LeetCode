""" 
Author: Aarya
Description: Given the head of a singly linked list, return the middle node of the linked list.
    If there are two middle nodes, return the second middle node.
Time Complexity: O(n), where n is the length of the linked list.
Space Complexity: O(1), the algorithm uses temp variables to keep track of the nodes, these variables only require constant space
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize 2 variables that reference the head variable
        # The fast variable moves twice as fast as the slow variable
        # When the fast variable reaches the end or None then the slow pointer will be at the middle value (half the distance)
        fast = slow = head
        # While the fast node and the next node to fast are not None, then keep iterating over the linked list
        while fast and fast.next:
            # Move slow by one
            slow = slow.next
            # Move fast by 2
            fast = fast.next.next
        # Return the slow pointer when the loop finishes executing as the slow pointer will be at the middle value
        return slow