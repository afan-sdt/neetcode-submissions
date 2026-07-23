class Solution:
    def isValid(self, s: str) -> bool:
        #iterate through array
        #if opening brace, add to stack
        #if closing brace see if top of stack matches

        stck = []
        for i in s:
            if i == '(' or i == '{' or i == '[':
                stck.append(i)
            elif i == ')':
                if not stck:
                    return False
                if stck.pop() != '(':
                    return False
            elif i == '}':
                if not stck:
                    return False
                if stck.pop() != '{':
                    return False
            elif i == ']':
                if not stck:
                    return False
                if stck.pop() != '[':
                    return False
        return not stck