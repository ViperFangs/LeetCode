""" 
Author: Aarya
Description: Given an array of strings strs, group the anagrams together. You can return the answer in any order.
    An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
    typically using all the original letters exactly once.
Time Complexity: O(m + n) where m is the number of strings and n is the length of each string
"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        create a new dictionary where the default value for each key is an empty list
        this values of this dictionary will be used to store the strings with the same key value
        we use defaultdict rather than {} because a defaultdict never raises a KeyError
        this is used to avoid an edge case where we try to access a key that is not initialized
        """
        result = defaultdict(list)
        
        for str in strs:
            """ 
            create a list of 26 values to hold values from a to z (initialize all values of the list with 0)
            we will increment the index of the character by 1 when we encounter it in the str
            """
            count = [0] * 26

            for char in str:
                """
                use ord to find the ASCII value of a character
                subtract the ASCII value of the current character with the ASCII value of the alphabet "a"
                this is done to achieve the index value for the list that will be incremented
                e.g. The character "c" has the ASCII value of 83, and the character "a" has the ASCII value of 80
                    83 - 80 will result to 3, which will be the index that will be incremented in the list
                """
                index = ord(char) - ord("a")
                count[index] += 1
            """
            convert the list into a tuple. e.g. [1, 0, 1] will be converted to (1, 0, 1)
            this is done because the key value for a dictonary cannot be a list.
            this will group each string that has the same list in the same key-value pair
            because we created a defaultdict above, we wont get a KeyError if we try to access a key that is not initialized
            e.g. eat and tea will have the same list: [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
                thus, eat and tea will be stored as the value for the key above
            """
            result[tuple(count)].append(str)
        # return the values of the hashmap, this will return a l
        return result.values()