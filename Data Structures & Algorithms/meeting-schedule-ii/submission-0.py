import heapq

class Solution:
    def minMeetingRooms(self, intervals):

        intervals.sort(key=lambda x: x.start)

        heap = []

        for interval in intervals:

            if heap and heap[0] <= interval.start:
                heapq.heappop(heap)

            heapq.heappush(heap, interval.end)

        return len(heap)