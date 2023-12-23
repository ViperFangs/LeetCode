""" 
Author: Aarya
Description: You are given the heads of two sorted linked lists list1 and list2.
    Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
    Return the head of the merged linked list.
Time Complexity: O(n), where n is the length of the linked lists
Space Complexity: O(1), the algorithm uses temp variables to keep track of the nodes, these variables only require constant space
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a ListNode object and store the reference in both the head and node variable, this creates a new ListNode
        head = node = ListNode()
        # While both the list are not None (Have a pointer reference stored in them)
        while list1 and list2:
            # If the current value at list1 is less than the value in list2, then add list1 to the new ListNode
            if list1.val < list2.val:
                node.next = list1
                # Go to the next ListNode in list1
                list1 = list1.next
            # If the current value at list2 is less than or equal to the current value at list1, then add list2 to the new ListNode
            else:
                node.next = list2
                # Go to the next ListNode in list2
                list2 = list2.next
            # Move node forward
            node = node.next
        # When either one of the list is exhausted then attach the non-exhausted list to the end of the new ListNode, both the lists are already sorted
        node.next = list1 or list2
        # return the next variable that is stored in the head variable as that contains the start of the new ListNode
        return head.next