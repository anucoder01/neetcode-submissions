class Solution:
    def splitArray(self, nums, k):
        low = max(nums)
        high = sum(nums)

        while low < high:
            mid = (low + high) // 2

            # Count how many subarrays we need
            subarrays = 1
            current_sum = 0

            for num in nums:
                if current_sum + num > mid:
                    subarrays += 1
                    current_sum = num
                else:
                    current_sum += num

            if subarrays <= k:
                high = mid
            else:
                low = mid + 1

        return low