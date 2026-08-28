class RandomizedSet:

    def __init__(self):
        self.indicies = {}
        self.vals = []

    def insert(self, val: int) -> bool:
        if val in self.indicies:
            return False
        self.vals.append(val)
        self.indicies[val] = len(self.vals) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.indicies:
            return False
        index = self.indicies[val]
        last = self.vals[-1]
        self.vals[index] = last
        self.vals.pop()
        self.indicies[last] = index
        del self.indicies[val]
        return True
    def getRandom(self) -> int:
        return random.choice(self.vals)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()