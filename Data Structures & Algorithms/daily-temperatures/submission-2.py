class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ret = [0] * len(temperatures)
        for i, temp in enumerate(temperatures):
            #(index, value)
            while stack and temp > stack[-1][1]:
                index, value = stack.pop()
                ret[index] = i - index
            tup = (i, temp)
            stack.append(tup)
        return ret

