class Solution:
    def minMeetingRooms(self, intervals):
        if not intervals:
            return 0

        starts = sorted(interval.start for interval in intervals)
        ends = sorted(interval.end for interval in intervals)

        start = 0
        end = 0
        rooms = 0
        max_rooms = 0

        while start < len(intervals):
            if starts[start] < ends[end]:
                # A meeting starts before another one ends
                rooms += 1
                max_rooms = max(max_rooms, rooms)
                start += 1
            else:
                # A meeting has ended, so reuse its room
                rooms -= 1
                end += 1

        return max_rooms