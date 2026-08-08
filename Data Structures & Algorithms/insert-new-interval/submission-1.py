class Solution:
    def insert(self, intervals, newInterval):
        ans = []

        for interval in intervals:
            # Current interval is completely before new interval
            if interval[1] < newInterval[0]:
                ans.append(interval)

            # Current interval is completely after new interval
            elif interval[0] > newInterval[1]:
                ans.append(newInterval)
                newInterval = interval

            # Overlapping intervals
            else:
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])

        ans.append(newInterval)
        return ans