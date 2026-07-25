class Solution:
    def missingNumber(self, nums):

        ans = len(nums)

        for i in range(len(nums)):
            ans = ans ^ i ^ nums[i]

        return ans