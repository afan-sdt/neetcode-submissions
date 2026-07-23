class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i == '{' or i == '[' or i== '(':
                stack.append(i)
            elif i == '}':
                if not stack or (stack and stack.pop() != '{'):
                    return False
            elif i == ']':
                if not stack or (stack and stack.pop() != '['):
                    return False
            elif i == ')':
                if not stack or (stack and stack.pop() != '('):
                    return False
        if len(stack) == 0:
            return True
        else:
            return False

        