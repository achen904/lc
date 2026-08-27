class Solution:
    def calculate(self, s: str) -> int:
        #need to skip white spaces
        #need to address for numbers greater than one digit
        #Use a stack to get previous number and store an operator
        #initialize operator to "+" as default

        num = 0
        op = "+"
        stack = []
        ops = set(["+", "-", "*", "/"])
        for i, ch in enumerate(s):
            if ch == " " and num == 0:
                continue
            elif ch not in ops and ch != " ":
                num = num * 10 + int(ch)
            if ch in ops or i == len(s) - 1:
                if op == "*":
                    stack.append(stack.pop() * num)
                elif op == "/":
                    stack.append(int(stack.pop() / num))
                elif op == "-":
                    stack.append(-num)
                else:
                    stack.append(num)
                num = 0
                op = ch
        return sum(stack)
            