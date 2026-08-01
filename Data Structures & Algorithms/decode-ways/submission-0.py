class Solution:
    def numDecodings(self, s):

        one = 1      # dp[i+1]
        two = 0      # dp[i+2]

        for i in range(len(s)-1, -1, -1):

            if s[i] == "0":
                curr = 0
            else:
                curr = one

                if i + 1 < len(s) and (
                    s[i] == "1" or
                    (s[i] == "2" and s[i+1] <= "6")
                ):
                    curr += two if i + 2 <= len(s)-1 else 1

            two = one
            one = curr

        return one