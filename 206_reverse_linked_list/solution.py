""" 
Author: Aarya
Description: Given the head of a singly linked list, reverse the list, and return the reversed list.
Time Complexity: O(n), where n is the size of the linked list
Space Complexity: O(1), The algorithm only initializes variables that dont grow with the input
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: [ListNode]) -> [ListNode]:
        # Define the previous and next nodes as None
        previous_node, next_node = None, None
        # Loop through the linked list
        while head != None:
            # Store a reference to the next node before editing the current head node
            next_node = head.next
            # Change the current node's parent to the previous node
            head.next = previous_node 
            # Update the previous_node as the current head node
            previous_node = head
            # Move head to the next node
            head = next_node
        """
        The loop exits after head is None
        Return the previous_node as it contains the reverse linked list
        """
        return previous_node