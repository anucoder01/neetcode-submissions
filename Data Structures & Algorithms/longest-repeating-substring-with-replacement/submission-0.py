class Solution:
    def characterReplacement(self, s, k):

        count = {}
        left = 0
        maxCount = 0
        ans = 0

        for right in range(len(s)):

            count[s[right]] = count.get(s[right], 0) + 1
            maxCount = max(maxCount, count[s[right]])

            while (right - left + 1) - maxCount > k:
                count[s[left]] -= 1
                left += 1

            ans = max(ans, right - left + 1)

        return ans