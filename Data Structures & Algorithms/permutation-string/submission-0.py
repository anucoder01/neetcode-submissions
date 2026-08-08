class Solution:
    def checkInclusion(self, s1, s2):

        # s1 cannot fit inside s2
        if len(s1) > len(s2):
            return False

        # Frequency of characters in s1
        count1 = [0] * 26

        # Frequency of characters in current window of s2
        count2 = [0] * 26

        for ch in s1:
            count1[ord(ch) - ord('a')] += 1

        # Create the first window
        for i in range(len(s1)):
            count2[ord(s2[i]) - ord('a')] += 1

        # If frequencies match, permutation exists
        if count1 == count2:
            return True

        # Sliding window
        for i in range(len(s1), len(s2)):

            # Add new character to the window
            count2[ord(s2[i]) - ord('a')] += 1

            # Remove character leaving the window
            count2[ord(s2[i - len(s1)]) - ord('a')] -= 1

            # Check if current window is a permutation of s1
            if count1 == count2:
                return True

        return False