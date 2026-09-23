class Solution:
    def checkValidString(self, s: str) -> bool:
        #greedy approach is to use * as a left parenthesis if we encounter a right parenthesis if we have no available left parenthesis
        #if neither a ( or a * then we can return false early
        #maintain 2 seperate stacks for ( and *, storing the indicies of each respectively
        #after processing the entirety of s, the 2 stacks might still be nonempty, if left parenthesis is nonempty, then we pop both stacks treating the * as a ) if the * index is greater than the ( index.
        #after this if only the * stack is nonempty we can treat it as empty spaces
        leftStack = []
        starStack = []

        for i, ch in enumerate(s):
            if ch == "(":
                leftStack.append(i)
            elif ch == "*":
                starStack.append(i)
            else:
                if leftStack:
                    leftStack.pop()
                elif starStack:
                    starStack.pop()
                else:
                    return False
        
        while leftStack:
            if starStack:
                leftInd = leftStack.pop()
                starInd = starStack.pop()
                if leftInd > starInd:
                    return False
            else:
                return False
        return True