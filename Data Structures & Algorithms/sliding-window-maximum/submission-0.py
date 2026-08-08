from collections import deque

class Solution:
    def maxSlidingWindow(self, nums, k):

        # Store indices of useful elements
        # Values are kept in decreasing order
        dq = deque()

        result = []

        for i in range(len(nums)):

            # Remove indices that are outside the window
            if dq and dq[0] < i - k + 1:
                dq.popleft()

            # Remove smaller elements from the back
            # because they can never be the maximum
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()

            # Add current index
            dq.append(i)

            # Window is ready once we have k elements
            if i >= k - 1:
                result.append(nums[dq[0]])

        return result