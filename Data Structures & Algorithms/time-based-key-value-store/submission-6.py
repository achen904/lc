class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        arr = self.map[key]
        if not arr:
            return ""
        if arr[len(arr) -1][0] < timestamp:
            return arr[len(arr) - 1][1]
        elif timestamp < arr[0][0]:
            return ""
        l = 0
        r = len(arr) - 1
        potential = -1
        while l <= r:
            m = (l + r) //2
            if arr[m][0] <= timestamp:
                potential = max(m, potential)
                if arr[m][0] == timestamp:
                    return arr[m][1]
                l = m + 1
            else:
                r = m - 1
        if potential != -1:
            return arr[potential][1]
        return arr[len(arr) - 1][1]

