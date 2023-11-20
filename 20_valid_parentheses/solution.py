""" 
Author: Aarya
Description: Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
    An input string is valid if:
        1. Open brackets must be closed by the same type of brackets.
        2. Open brackets must be closed in the correct order.
        3. Every close bracket has a corresponding open bracket of the same type.
Time Complexity: O(n), where n is the length of the string
"""
class Solution:
    def isValid(self, s: str) -> bool:
        # intialize an empty stack to store open brackets
        stack = []
        """
        create a hashmap that stores the closing brackets as the key and the opening brackets as the values
        this will be utilized later to check for valid parentheses
        key => closing bracket, value => opening bracket
        """
        bracket_map = {")" : "(", "}" : "{", "]" : "["}
        # loop through the string
        for bracket in s:
            """
            if the current bracket is one of the opening brackets then add it to the stack
            all the opening brackets are stored as the values in the bracket_map
            """
            if bracket in bracket_map.values():
                stack.append(bracket)
            # if the current bracket is not an opening bracket then it must be a closing bracket
            else:
                """
                if the stack is empty or
                if the closing bracket is not the same as it's corresponding opening bracket then return False
                    - use stack.pop() to pop out(remove) the last item in the stack
                e.g. if the current bracket is "]" and the bracket that was popped out isn't "[", then return False
                """
                if not stack or stack.pop() != bracket_map[bracket]:
                    return False
        """
        if the stack is empty by the end of the string then return True, as all brackets are closed
        if the stack is not empty by the end of the string then return False, 
            as there some open brackets are still present in the stack
        """
        return True if not stack else False
