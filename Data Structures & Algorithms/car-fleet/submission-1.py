class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #create a stack of fleets with shortest to longest time
        #lenght of stack is the number of fleets
        #sort by highest position since cars cannot pass eachother
        #so the fleet is limited to the time of the car at the highest
        #position
        merged = list(zip(position, speed))
        merged.sort(reverse=True)
        stack = []
        for p, s in merged:
            time = (target - p)/s
            if not stack or time > stack[-1]:
                stack.append(time)
        return len(stack)