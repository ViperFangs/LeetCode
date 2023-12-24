""" 
Author: Aarya
Description: Given head, the head of a linked list, determine if the linked list has a cycle in it.
    There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. 
    Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.
    Return true if there is a cycle in the linked list. Otherwise, return false.
Time Complexity: O(n), where n is the length of the linked list.
Space Complexity: O(1), the algorithm uses temp variables to keep track of the nodes, these variables only require constant space
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Initialize 2 variables that reference the head variable
        # The fast variable moves twice as fast as the slow variable
        fast = slow = head
        # While the fast node and the next node to fast are not None, then keep iterating over the linked list
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            # If fast is ever the same as slow then return True as this can only happen if there is a cycle
            if fast == slow:
                return True
        # return False if the loop finished executing as there is no cycle
        return False