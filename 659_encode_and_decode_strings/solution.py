""" 
Author: Aarya
Description: Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.
    Please implement encode and decode methods
Time Complexity: O(n) for encode, where n is the size of the list
                 O(n) for decode, where n is the length of the string
"""
class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        # initialize an empty string
        result = ""
        # loop through the list of string
        for s in strs:
            """
            add encoding data to the string and append to the result string
            e.g. "leet" will be changed to "4#leet". "abcdefghijk" will be encoded to "11#abcdefghijk"
                the number signifies the length of the string and the # sign is used a delimiter
                the decode function can use information this for decoding the string
            """
            result += str(len(s)) + "#" + s
        return result
            
    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """
    def decode(self, str):
        # initialize i to 0 (start of the string)
        i = 0
        # initialize an empty list which will store the decoded strings
        result = []
        # create a loop till the end of the string
        while i < len(str):
            # set j to the current position of i
            j = i
            """
            loop through the string using j until it finds "#" (the delimeter)
            we can use this to get the length of the string
            """
            while(str[j] != "#"):
                # increment j if the the value at the current position isnt a "#"
                j += 1
            """
            i will be at the start of the length and j will be at the "#" at this point
            we can make a substring from i and j and convert it into an int to get the length of the string after the "#"
            e.g. "11#abcdefghijk" i will be at the initial "1" and j will be at the "#",
                creating a substring(slice) from i's position to j's position will return "11" which is the length of "abcdefghijk"
            """
            # get the length of the current string
            length = int(str[i:j])
            # set i to j + 1 (after the # delimter)
            i = j + 1
            # set j to the end of the current string using i + length
            j = i + length
            # create a slice from i's position to j's position and add that to the result list
            result.append(str[i: j])
            """
            set i to the end of the string, this will make i go to the start of the next string
            e.g. "4#leet11#abcdefghijk", after appending the string "leet" to the list, i will be set to "1"
                this will be used to find the length of the next string and will repeat until the end of the string length 
            """
            i = j
        # return result as it will contain all the decoded strings
        return result