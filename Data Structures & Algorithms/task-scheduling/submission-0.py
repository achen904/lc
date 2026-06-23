class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #gets counts of each task
        # add tuple of (count, task) to heap
        # while loop to make sure we abide by wait time
        counts = defaultdict(int)
        for task in tasks:
            counts[task] -= 1
        heap = list(counts.values())
        heapq.heapify(heap)
        time = 0
        while heap:
            buffer = []
            cycle = 0
            while heap and cycle < n + 1:
                value = heapq.heappop(heap) + 1
                if value < 0:
                    buffer.append(value)
                cycle += 1
            if not buffer:
                time += cycle
            else:
                time += n + 1
            for task in buffer:
                heapq.heappush(heap, task)
        return time
            
