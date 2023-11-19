""" 
Author: Aarya
Description: Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
    You must write an algorithm that runs in O(n) time.
Time Complexity: O(n) where n is the size of nums
"""
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # create a set of using the nums list, this will remove all duplicates
        hashset = set(nums)
        # initialize longest to 0
        longest = 0
        # loop through the hashset
        for n in hashset:
            """
            if the "current number - 1" is not in the hashset then that signifies the start of a new sequence
            e.g. [100,4,200,1,3,2], for the value 100, we check if 99 is in the set.
                If not then that means 100 is the start of a new sequence
            """
            if(n - 1) not in hashset:
                # initialize length = 1 for the new sequence
                length = 1
                """
                check if the n + length is in the hashset
                we use n + length as length will be incremented each time the while loop executes
                this loop will continue until the end of the current consecutive sequence
                """
                while (n + length) in hashset:
                    # if n + length is present in the hashset then increment the length by 1
                    length += 1
                # after the loop, compare the previous longest with the current length and store the bigger value
                longest = max(longest, length)
        # return the length of the longest consecutive sequence
        return longest