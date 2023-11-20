class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracketMap = {")" : "(", "}" : "{", "]" : "["}

        for bracket in s:
            if bracket in bracketMap.values():
                stack.append(bracket)
            else:
                if not stack or stack.pop() != bracketMap[bracket]:
                    return False
        return True if not stack else False
