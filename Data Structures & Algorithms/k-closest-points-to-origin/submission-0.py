import heapq

class Solution:
    def kClosest(self, points, k):

        # Max heap to keep the k closest points
        # Store (-distance, point) because Python has a min heap
        heap = []

        for x, y in points:

            # Squared distance from origin
            distance = x * x + y * y

            # Add point to heap
            heapq.heappush(heap, (-distance, x, y))

            # Keep only k closest points
            if len(heap) > k:
                heapq.heappop(heap)

        # Extract the points from the heap
        return [[x, y] for distance, x, y in heap]