""" 
Author: Aarya
Description: Given a string s, find the length of the longest substring without repeating characters.
Time Complexity: O(n), where n is the length of the string
Space Complexity: O(n), The algorithm uses a hashset that could be as large as s
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
            # Initialize the left pointer at the start of the string
            l = 0
            # Initialize a hashset that will store all the non-duplicate characters in str s
            window = set()
            # Initialize a variable that will store the max length of the substring
            max_length = 0
            # Loop through the string using the right pointer
            for r in range(len(s)):
                """
                if the current value at the right pointer is present in the hashset, then remove the values from the hashset using the left pointer
                    The algorithm will keep removing values from the left pointer until the value at the right pointer isn't in the hashset
                This is done to find the longest substring
                """
                while s[r] in window:
                    # remove the value at the left pointer from the hashset
                    window.remove(s[l])
                    # increment the left pointer
                    l += 1
                # Add the character at the right pointer to the hashset
                window.add(s[r])
                # Change the variable max_length if the current length of the hashset is greater than max_length
                max_length = max(len(window), max_length)
            # Return the length of the longest substring
            return max_length