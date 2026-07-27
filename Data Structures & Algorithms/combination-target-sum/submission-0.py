class Solution:
    def combinationSum(self, nums, target):

        ans = []

        def backtrack(i, cur, total):

            if total == target:
                ans.append(cur.copy())
                return

            if i == len(nums) or total > target:
                return

            # Take current number
            cur.append(nums[i])
            backtrack(i, cur, total + nums[i])

            # Backtrack
            cur.pop()

            # Skip current number
            backtrack(i + 1, cur, total)

        backtrack(0, [], 0)

        return ans