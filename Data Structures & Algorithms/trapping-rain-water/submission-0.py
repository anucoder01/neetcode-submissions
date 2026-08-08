class Solution:
    def trap(self, height):

        # Two pointers
        left = 0
        right = len(height) - 1

        # Maximum height seen from left and right
        leftMax = 0
        rightMax = 0

        water = 0

        while left < right:

            # Left side is smaller
            if height[left] <= height[right]:

                # Update left maximum
                if height[left] >= leftMax:
                    leftMax = height[left]
                else:
                    # Water trapped at left
                    water += leftMax - height[left]

                left += 1

            # Right side is smaller
            else:

                # Update right maximum
                if height[right] >= rightMax:
                    rightMax = height[right]
                else:
                    # Water trapped at right
                    water += rightMax - height[right]

                right -= 1

        return water