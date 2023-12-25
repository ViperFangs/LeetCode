""" 
Author: Aarya
Description: In a linked list of size n, where n is even, the ith node (0-indexed) of the linked list is known as the twin of the (n-1-i)th node, if 0 <= i <= (n / 2) - 1.
    For example, if n = 4, then node 0 is the twin of node 3, and node 1 is the twin of node 2. These are the only nodes with twins for n = 4.
    The twin sum is defined as the sum of a node and its twin.
    Given the head of a linked list with even length, return the maximum twin sum of the linked list.
Time Complexity: O(n), where n is the length of the linked list.
Space Complexity: O(1), the algorithm uses temp variables to keep track of the nodes, these variables only require constant space
Logic: The logic for this solution is to reverse the linked list until the midpoint. 
    One variable will be used to traverse from the midpoint to the end.
    Second variable will be used to traverse from the midpoint - 1 to the start
    The sum of the values at the first and second variable will be used to find the twin sum. 
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # Initialize variables to reference the head variable
        slow = fast = head
        # The slow_tail variable will be one node behind the slow variable, it will be used to reverse the first half of the list
        slow_tail = None
        # Initialize a variable that will hold the max twin sum value for the linked list
        max_sum = 0
        # Keep iterating through the linked list until fast is at the last value of the linked list
        while fast and fast.next:
            # It's important to perform this step at the beginning before reversing the the linked list
            fast = fast.next.next
            # Initialize a variable to hold the next node that comes after the slow pointer
            temp_node = slow.next
            # Reverse the link of the node at slow's position
            slow.next = slow_tail
            # Increment the slow_tail to follow slow
            slow_tail = slow
            # Move slow to the next node
            slow = temp_node
        # Use slow to iterate till the end, and use slow_tail to iterate till the beginning
        while slow and slow_tail:
            # Store the max twin sum value in the max_sum variable
            max_sum = max(slow.val + slow_tail.val, max_sum)
            # Move slow and slow_tail to the next node
            slow = slow.next
            slow_tail = slow_tail.next
        # Return the maximum twin sum
        return max_sum