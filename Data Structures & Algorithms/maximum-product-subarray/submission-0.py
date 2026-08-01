class Solution:
    def maxProduct(self, nums):

        res = nums[0]

        curMax = nums[0]
        curMin = nums[0]

        for i in range(1, len(nums)):

            num = nums[i]

            temp = curMax

            curMax = max(
                num,
                temp * num,
                curMin * num
            )

            curMin = min(
                num,
                temp * num,
                curMin * num
            )

            res = max(res, curMax)

        return res