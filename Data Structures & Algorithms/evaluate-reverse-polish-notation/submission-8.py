class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #two cases: operand or operator
        #operand: throw it onto the stack
        #operator: pop last two and perform operation. append result onto stack
        stck = []
        for thing in tokens:
            if thing == '+':
                op1 = stck.pop()
                op2 = stck.pop()
                res = op2 + op1
                stck.append(res)
            elif thing == '-':
                op1 = stck.pop()
                op2 = stck.pop()
                res = op2 - op1
                stck.append(res)
            elif thing == '*':
                op1 = stck.pop()
                op2 = stck.pop()
                res = op2 * op1
                stck.append(res)
            elif thing == '/':
                op1 = stck.pop()
                op2 = stck.pop()
                res = int(op2/op1)
                stck.append(res)
            else:
                stck.append(int(thing))
        return stck.pop()
