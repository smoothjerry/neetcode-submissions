class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {
            "+": lambda a, b: int(a) + int(b),
            "-": lambda a, b: int(a) - int(b),
            "*": lambda a, b: int(a) * int(b),
            "/": lambda a, b: int(int(a) / int(b))
        }

        stack = []
        for token in tokens:
            if token in operators:
                operator = operators[token]
                b, a = stack.pop(), stack.pop()
                res = operator(a, b)
                stack.append(res)
            else:
                stack.append(token)
        
        return int(stack.pop())