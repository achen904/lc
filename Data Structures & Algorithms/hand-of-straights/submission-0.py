class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()
        freqs = defaultdict(int)
        for val in hand:
            freqs[val] += 1
        
        for val in hand:
            if freqs[val] == 0:
                continue
            for i in range(groupSize):
                if freqs[val + i] > 0:
                    freqs[val + i] -= 1
                else:
                    return False
        return True

