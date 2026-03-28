class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])

        stack = []

        for i in range(len(tokens)):
            if tokens[i] == '+':
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(num1+num2)
            elif tokens[i] == '-':
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(num1-num2)
            elif tokens[i] == '*':
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(num1*num2)
            elif tokens[i] == '/':
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(int(num1/num2))
            else:
                stack.append(int(tokens[i]))

        return stack[0]