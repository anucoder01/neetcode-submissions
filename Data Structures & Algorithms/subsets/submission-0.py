class Solution:
    def subsets(self, nums):

        result = []

        def backtrack(index, current):

            # Add the current subset
            result.append(current.copy())

            # Try including each remaining number
            for i in range(index, len(nums)):

                # Choose
                current.append(nums[i])

                # Explore
                backtrack(i + 1, current)

                # Undo choice
                current.pop()

        backtrack(0, [])

        return result