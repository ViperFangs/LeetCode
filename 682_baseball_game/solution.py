""" 
Author: Aarya
Description: You are keeping the scores for a baseball game with strange rules. At the beginning of the game, you start with an empty record.
    You are given a list of strings operations, where operations[i] is the ith operation you must apply to the record and is one of the following:
        1. An integer x.
            Record a new score of x.
        2. '+'.
            Record a new score that is the sum of the previous two scores.
        3. 'D'.
            Record a new score that is the double of the previous score.
        4. 'C'.
            Invalidate the previous score, removing it from the record.
        Return the sum of all the scores on the record after applying all the operations.
    The test cases are generated such that the answer and all intermediate calculations fit in a 32-bit integer and that all operations are valid.
Time Complexity: O(n), where n is the length of the operations list.
Space Complexity: O(n), the algorithm uses a stack to do the operations
Logic: The logic here is to use a stack(a list in python) to do the operations, and then return the sum of the stack
"""
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for op in operations:
            match op:
                case "C":
                    stack.pop()
                case "D":
                    stack.append(stack[-1] * 2)
                case "+":
                    stack.append(stack[-1] + stack[-2])
                case _:
                    stack.append(int(op))
        return sum(stack)