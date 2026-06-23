class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            if ch == "(" or ch == "[" or ch == "{":
                stack.append(ch)
            else:
                if not stack:
                    return False
                ret = stack.pop()
                if ch == "}" and ret != "{":
                    return False
                elif ch == "]" and ret != "[":
                    return False
                elif ch == ")" and ret != "(":
                    return False
        if not stack:
            return True
        return False