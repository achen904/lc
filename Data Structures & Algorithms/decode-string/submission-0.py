class Solution:
    def decodeString(self, s: str) -> str:
        #need to know the previous number to determine how appends
        #need to know old string to append new ones to it
        sStack = []
        nStack = []
        num = 0 
        ans = ""

        for i in range(len(s)):
            if s[i].isdigit():
                num = num * 10 + int(s[i])
            elif s[i] == "[":
                #add current string to stack and start buildig new to add to it later
                sStack.append(ans)
                nStack.append(num)
                num = 0
                ans = ""
            elif s[i] == "]":
                #store our current 
                temp = ans
                ans = sStack.pop()
                n = nStack.pop()
                ans += temp * n
            else:
                ans += s[i]
        return ans