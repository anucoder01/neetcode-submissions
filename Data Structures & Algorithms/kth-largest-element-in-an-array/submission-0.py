import heapq

class Solution:
    def findKthLargest(self, nums, k):

        # Min heap stores the k largest elements
        heap = []

        for num in nums:

            # Add current number
            heapq.heappush(heap, num)

            # Keep only k largest elements
            if len(heap) > k:
                heapq.heappop(heap)

        # Smallest among the k largest = kth largest
        return heap[0]