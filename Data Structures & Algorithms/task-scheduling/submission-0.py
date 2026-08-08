from collections import Counter
import heapq
from collections import deque

class Solution:
    def leastInterval(self, tasks, n):

        # Count frequency of each task
        count = Counter(tasks)

        # Max heap using negative frequencies
        heap = [-freq for freq in count.values()]
        heapq.heapify(heap)

        # Queue stores:
        # [remaining_frequency, time_when_available]
        q = deque()

        time = 0

        while heap or q:
            time += 1

            # If a task is available, execute the most frequent one
            if heap:
                freq = heapq.heappop(heap)
                freq += 1  # Since frequencies are negative

                # If task still has remaining occurrences,
                # put it in cooldown
                if freq != 0:
                    q.append((freq, time + n))

            # Move tasks whose cooldown is finished back to heap
            if q and q[0][1] == time:
                freq, available_time = q.popleft()
                heapq.heappush(heap, freq)

        return time