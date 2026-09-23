class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        x, y, z = target
        prevA, prevB, prevC = triplets[0]
        i = 0
        while i + 1< len(triplets) and (prevA > x or prevB > y or prevC > z):
            newA, newB, newC = triplets[i + 1]
            if newA <= x and newB <= y and newC <= z:
                 prevA, prevB, prevC = newA, newB, newC
            i += 1
        for j in range(i, len(triplets)):
            a, b, c = triplets[j]
            if a > x or b > y or c > z:
                continue
            if a == x or b == y or c == z:
                triplets[j] = [max(a, prevA), max(b, prevB), max(c, prevC)]
                if triplets[j] == target:
                    return True
                prevA, prevB, prevC = triplets[j]
        return False