class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            print(stack)
            print(i)
            if i != '+' and i != '-' and i!= '*' and i !='/':
                stack.append(int(i))
                continue;
            op2 = stack.pop()
            op1 = stack.pop()
            if i == '+':
                stack.append(op1 + op2)
            elif i == '-':
                stack.append(op1 - op2)
            elif i == '*':
                stack.append(op1 * op2)
            elif i == '/':
                stack.append(int(float(op1) / op2))
        return stack.pop()

            