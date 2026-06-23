class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for p in s:
            if p == "}":
                if not stack or stack.pop() != "{":
                    return False
            elif p == ")":
                if not stack or stack.pop() != "(":
                    return False
            elif p == "]":
                if not stack or stack.pop() != "[":
                    return False
            else:
                stack.append(p)
        if not stack:
            return True
        return False

        