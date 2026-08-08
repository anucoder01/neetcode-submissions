import heapq

class Solution:
    def minMeetingRooms(self, intervals):

        # Process meetings in start-time order
        intervals.sort(key=lambda x: x.start)

        # Store when each occupied room becomes free
        heap = []

        for interval in intervals:

            # If a room is free, reuse it
            if heap and heap[0] <= interval.start:
                heapq.heappop(heap)

            # Occupy a room until this meeting ends
            heapq.heappush(heap, interval.end)

        # Number of occupied rooms
        return len(heap)