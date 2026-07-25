class Solution:
    def rob(self, nums):

        if len(nums) == 1:
            return nums[0]

        return max(self.helper(nums[:-1]), self.helper(nums[1:]))

    def helper(self, nums):

        rob1 = 0
        rob2 = 0

        for money in nums:
            newRob = max(rob1 + money, rob2)
            rob1 = rob2
            rob2 = newRob

        return rob2