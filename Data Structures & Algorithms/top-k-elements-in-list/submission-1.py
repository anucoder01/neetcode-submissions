class Solution:
    def topKFrequent(self, nums, k):

        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1

        sorted_count = sorted(count, key=count.get, reverse=True)

        return sorted_count[:k]