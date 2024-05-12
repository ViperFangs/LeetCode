""" 
Author: Aarya
Description: Given two strings s and t, return true if t is an anagram of s, and false otherwise.
    An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
    typically using all the original letters exactly once.
Time Complexity: O(s + t) or O(n) 
Space Complexity: O(n)
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if the length of both the strings isnt the same then return false
        if len(s) != len(t):
            return False
        # create 2 hashmaps that store the key as each character and the count as the value
        countS, countT = {}, {}
        """
        loop through the string length
        because both the strings should be the same length, we loop through them at the same time
        """
        for i in range(len(s)):
            """
            We use the get function in the case that a key is null and if it is then the get function will return 0,
            else it will return the value of the key
            """
            countS[s[i]] = countS.get(s[i], 0) + 1
            countT[t[i]] = countT.get(t[i], 0) + 1

        for c in countS:
            # if the value of the keys are not the same then return false
            if countS[c] != countT.get(c):
                return False
        # if the program has not returned false, then s is an anagram of t
        return True