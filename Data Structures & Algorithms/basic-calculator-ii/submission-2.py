class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        ops = set(["*", "+", "-", "/"])
        op = "+"
        i = 0
        num = 0
        for i, ch in enumerate(s):
            if s[i] == " " and num == 0:
                continue
            if s[i] not in ops and s[i] != " ":
                num = (num * 10) + int(s[i])
            if s[i] in ops or i == len(s) - 1:
                if op == "/":
                    prev = stack.pop()
                    stack.append(int(prev / num))
                elif op == "*":
                    prev = stack.pop()
                    stack.append(prev * num)
                elif op == "-":
                    stack.append(-num)
                else:
                    stack.append(num)
                op = s[i]
                num = 0
        return sum(stack)


