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