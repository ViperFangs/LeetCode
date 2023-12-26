""" 
Author: Aarya
Description: Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
    Implement the MinStack class:
        MinStack() initializes the stack object.
        void push(int val) pushes the element val onto the stack.
        void pop() removes the element on the top of the stack.
        int top() gets the top element of the stack.
        int getMin() retrieves the minimum element in the stack.
    You must implement a solution with O(1) time complexity for each function.
Time Complexity: O(n), where n is the length of the operations list.
Space Complexity: O(n), the algorithm uses a stack to do the operations
Logic: The logic here is to use a stack(a list in python) and a min_stack. The min stack keeps track of the lowest value for each element as they are added.
    The min_stack is needed to do the getMin() operation in O(1) time.
"""
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        # If the min_stack isn't empty then use the last value in it to find the new minimum
        if self.min_stack:
            val = min(val, self.min_stack[-1])
        self.min_stack.append(val)

    def pop(self) -> None:
        # Pop from both stack and min_stack
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]  

    def getMin(self) -> int:
        # The top value in the min_stack keeps track of the lowest value in the stack
        return self.min_stack[-1]
        
# The MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()