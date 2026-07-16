class Solution:
    def groupAnagrams(self, strs):
        d = {}

        for word in strs:
            key = "".join(sorted(word))
            d.setdefault(key, []).append(word)

        return list(d.values())