class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs: str):
        result = ""
        for s in strs:
            result += str(len(s)) + "#" + s
        return result
            
    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """
    def decode(self, str: str):
        # write your code here
        i = 0
        result = []
        
        while i < len(str):
            j = i
            while(str[j] != "#"):
                j += 1
            length = int(str[i:j])
            i = j + 1
            j = i + length
            result.append(str[i: j])
            i = j
        return result