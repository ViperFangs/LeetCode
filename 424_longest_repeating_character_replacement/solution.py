""" 
Author: Aarya
Description: You are given a string s and an integer k. 
    You can choose any character of the string and change it to any other uppercase English character. 
    You can perform this operation at most k times.
    Return the length of the longest substring containing the same letter you can get after performing the above operations.
Time Complexity: O(n), where n is the size of the nums list
Space Complexity: O(k), The algorithm uses a dict that can grow as large as k
"""
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Initialize a left pointer at the start of the string
        l = 0
        # Initialize output as 0, this variable tracks the length of the longest substring
        output = 0
        # Create a hashmap that stores the count of each character in the string
        character_count = {}
        # loop through the string using the right pointer
        for r in range(len(s)):
            # Increment the count of the current character by 1 in the hashmap
            character_count[s[r]] =  character_count.get(s[r], 0) + 1
            """
            If the "length of the window - the most occurring character in the hashmap" is greater than K, then:
                Reduce the count of the character that's at the left pointer
                Increment the left pointer by 1
            This check is performed to see if the amount of character changes in the substring would exceed K
            """
            if (r - l + 1) - max(character_count.values()) > k:
                character_count[s[l]] -= 1
                l += 1
            # If the current length of the window is greater than the stored output value, then update the output
            output = max(output, r - l + 1)
        # Return the length of the longest substring containing the same letter you can get after changing the characters K times.
        return output