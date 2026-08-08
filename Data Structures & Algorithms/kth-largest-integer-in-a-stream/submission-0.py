import heapq

class KthLargest:

    def __init__(self, k, nums):
        self.k = k

        # Min heap stores the k largest elements
        self.heap = []

        # Add all initial numbers
        for num in nums:
            heapq.heappush(self.heap, num)

            # Keep only k largest elements
            if len(self.heap) > k:
                heapq.heappop(self.heap)

    def add(self, val):

        # Add new value to the heap
        heapq.heappush(self.heap, val)

        # Keep only k largest elements
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)

        # Smallest element among the k largest
        # is the kth largest element
        return self.heap[0]