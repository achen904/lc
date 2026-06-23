class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        combined = list(zip(position, speed))
        combined.sort(reverse=True)
        stack = []
        for position, speed in combined:
            time = (target - position)/speed
            if not stack or time > stack[-1]:
                stack.append(time)
        return len(stack)
