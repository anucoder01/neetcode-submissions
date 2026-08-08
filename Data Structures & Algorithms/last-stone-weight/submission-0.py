import heapq

class Solution:
    def lastStoneWeight(self, stones):

        # Python has a min heap, so use negative values
        # to simulate a max heap
        heap = [-stone for stone in stones]
        heapq.heapify(heap)

        while len(heap) > 1:

            # First popped = heaviest stone
            x = -heapq.heappop(heap)

            # Second popped = second heaviest
            y = -heapq.heappop(heap)

            # If they are different, the remaining stone
            # has weight x - y
            if x != y:
                heapq.heappush(heap, -(x - y))

        # Return the remaining stone, or 0 if none remain
        return -heap[0] if heap else 0