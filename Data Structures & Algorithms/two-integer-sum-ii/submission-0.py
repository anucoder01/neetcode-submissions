class Solution:
    def twoSum(self, numbers, target):

        # Two pointers
        left = 0
        right = len(numbers) - 1

        while left < right:

            total = numbers[left] + numbers[right]

            # Found the target
            if total == target:
                return [left + 1, right + 1]

            # Sum is too small → move left pointer right
            elif total < target:
                left += 1

            # Sum is too large → move right pointer left
            else:
                right -= 1