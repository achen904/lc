class MedianFinder:

    def __init__(self):
        self.heap1 = [] #max
        self.heap2 = [] #min
        #min should be greater than max
        heapq.heapify(self.heap1)
        heapq.heapify(self.heap2)

    def addNum(self, num: int) -> None:
        if not self.heap1 and not self.heap2:
            heapq.heappush(self.heap1, -num)
        elif self.heap1 and not self.heap2:
            if num >= -self.heap1[0]:
                heapq.heappush(self.heap2, num)
            else:
                heapq.heappush(self.heap2, -heapq.heappop(self.heap1))
                heapq.heappush(self.heap1, -num)

        else:
            if num > -self.heap1[0] and num < self.heap2[0]:
                if len(self.heap1) > len(self.heap2):
                    heapq.heappush(self.heap2, -heapq.heappop(self.heap1))
                    heapq.heappush(self.heap1, -num)
                else:
                    heapq.heappush(self.heap1, -num)
            elif num < -self.heap1[0]:
                if len(self.heap1) > len(self.heap2):
                    heapq.heappush(self.heap2, -heapq.heappop(self.heap1))
                    heapq.heappush(self.heap1, -num)
                else:
                    heapq.heappush(self.heap1, -num)
            else:
                if len(self.heap2) > len(self.heap1):
                    heapq.heappush(self.heap1, -heapq.heappop(self.heap2))
                    heapq.heappush(self.heap2, num)
                else:
                    heapq.heappush(self.heap2, num)

    def findMedian(self) -> float:
        if len(self.heap1) == len(self.heap2):
            return (-self.heap1[0] + self.heap2[0])/2
        elif len(self.heap1) > len(self.heap2):
            return -self.heap1[0]
        return self.heap2[0]
        
        