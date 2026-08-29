class Solution:
    def decodeString(self, s: str) -> str:
        ans = ""
        #need a stack for the number and a stack for the cur string
        #once we see a closing paranthesis, we pop from both stacks to get previous string and append cur string the number of times from numstack
        #we add to numstack and string stacks once we see an openining paranthesis
        #other wise we add to ans for string

        numStack = []
        stringStack = []
        num = 0
        for ch in s:
            if ch == "[":
                numStack.append(num)
                stringStack.append(ans)
                num = 0
                ans = ""
            elif ch == "]":
                n = numStack.pop()
                temp = ans
                ans = stringStack.pop()
                ans += temp * n
            elif ch.isdigit():
                num = 10 *num + int(ch)
            else:
                ans += ch
        return ans