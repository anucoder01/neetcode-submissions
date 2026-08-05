class Solution:
    def isPalindrome(self, s: str) -> bool:
        news = ""

        for char in s:
            if char.isalnum():
                news += char.lower()

        return news == news[::-1]