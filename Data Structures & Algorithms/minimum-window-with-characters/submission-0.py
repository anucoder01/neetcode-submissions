class Solution:
    def minWindow(self, s, t):

        need = {}
        for ch in t:
            need[ch] = need.get(ch, 0) + 1

        left = 0
        count = len(t)

        start = 0
        minLen = float("inf")

        for right in range(len(s)):

            if s[right] in need:
                if need[s[right]] > 0:
                    count -= 1
                need[s[right]] -= 1

            while count == 0:

                if right - left + 1 < minLen:
                    minLen = right - left + 1
                    start = left

                if s[left] in need:
                    need[s[left]] += 1
                    if need[s[left]] > 0:
                        count += 1

                left += 1

        if minLen == float("inf"):
            return ""

        return s[start:start + minLen]