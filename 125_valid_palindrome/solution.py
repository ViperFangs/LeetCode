"""
Author: Aarya
Description: A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
    Given a string s, return true if it is a palindrome, or false otherwise.
Time Complexity: O(n), where n is the length of the str string
Space Complexity: O(1), the solution uses a couple integers that don't grow with the input.
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # create a left pointer at the start of the string
        l = 0
        # create a right pointer at the end of the string
        r = len(s) - 1
        # loop through the string until the left pointer becomes greater than the right pointer 
        while l < r:
            # while the current character at the left pointer is not an alphanumeric then increment the left pointer
            while l < r and not s[l].isalnum():
                l += 1
            # while the current character at the right pointer is not an alphanumeric then decrement the right pointer
            while r > l and not s[r].isalnum():
                r -= 1
            # if the character at the left pointer is not the same as the character at the right pointer then return False
            if s[l].lower() != s[r].lower():
                return False
            # increment the left pointer and decrement the right pointer
            l, r = l + 1, r - 1
        # if the code hasn't returned False by now then the string is a palindrome: return True
        return True
    # alternate implmentation for the solution, requires O(n) space
    def isPalindromeP(self, s: str) -> bool:
        # create an empty string
        seq = ""
        # loop through the parameter str
        for c in s:
            # if the current character is alphanumeric then append it to the str
            if c.isalnum():
                seq += c.lower()
        # Check if the reverse string is the same as the forward string. return True if it's the same, else return false
        return seq == seq[::-1]
        