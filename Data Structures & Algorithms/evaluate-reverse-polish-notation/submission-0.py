class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        signs = {"+": lambda a, b: a + b,
                 "-": lambda a, b: a - b, 
                 "*": lambda a, b: a * b, 
                 "/": lambda a, b: a / b}
        stack = []
        for i in tokens:
            if i in signs.keys():
                right = int(stack.pop())
                left = int(stack.pop())
                res = signs[i](left, right)
                stack.append(res)
            else:
                stack.append(i)
        # print(stack)
        return int(stack.pop())

