class Solution:
    def eraseOverlapIntervals(self, intervals):
        intervals.sort(key=lambda x: x[1])   # Sort by end time

        end = intervals[0][1]
        count = 0

        for start, finish in intervals[1:]:
            if start < end:          # Overlapping
                count += 1
            else:                    # Non-overlapping
                end = finish

        return count