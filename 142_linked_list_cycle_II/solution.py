""" 
Author: Aarya
Description: Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.
    There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. 
    Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. 
    Note that pos is not passed as a parameter. Do not modify the linked list.
Time Complexity: O(n), where n is the length of the linked list.
Space Complexity: O(1), the algorithm uses temp variables to keep track of the nodes, these variables only require constant space
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Create variables to hold the reference of the head pointer
        fast = slow = cycle_start = head
        # Use the slow and fast pointer to find the cycle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            # Once a cycle has been found, find the index of the node at the start of the cycle
            if slow == fast:
                """ 
                The math from Floyd's Tortoise and Hare Algorithm says that:
                    The distance from where the slow and fast pointer meet to the start of the cycle 
                    is the same distance from the head of the Linked list to the start of the cycle
                """
                while slow != cycle_start:
                    slow = slow.next
                    cycle_start = cycle_start.next
                # The loop above will terminate when slow and cycle_start are the same, this happens at the start of the cycle
                return cycle_start
        # return None if a cycle doesn't exist
        return None