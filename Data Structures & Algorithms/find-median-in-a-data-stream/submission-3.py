class MedianFinder:

    def __init__(self):
        #have 2 heaps, 1 min heap and 1 max heap, the max heap stores the smaller half of current numbers and the min heap stores the larger half of the numbers, so that way when we look at the top of each heap we get the largest number from smaller half and smallest number from larger half. need to make sure that that heaps are equal sized or differ by at most 1 for odd total numbers
        #if odd numbers, the minHeap will always store the extranumber and therefore the median
        self.minHeap = [] #1
        self.maxHeap = [] #

    def addNum(self, num: int) -> None:
        if not self.minHeap and not self.maxHeap:
            heapq.heappush(self.minHeap, num)
        elif not self.maxHeap:
            if num > self.minHeap[0]:
                heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))
                heapq.heappush(self.minHeap, num)
            else:
                heapq.heappush(self.maxHeap, -num)
        else:
            topMin = self.minHeap[0]
            topMax = -self.maxHeap[0]
            if num < topMax:
                heapq.heappush(self.maxHeap, -num)
                if len(self.maxHeap) > len(self.minHeap):
                    heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))
            else: #num > topMin:
                heapq.heappush(self.minHeap, num)
                if len(self.minHeap) > len(self.maxHeap) + 1:
                    heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))

        

    def findMedian(self) -> float:
        if len(self.maxHeap) == len(self.minHeap):
            return ((-self.maxHeap[0]) + (self.minHeap[0]))/2
        else:
            return self.minHeap[0]
        
        