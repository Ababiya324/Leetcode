class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        if len(s) < 2:
            return s

        def pal(s, l, r):
            while l < r:
                if s[l] != s[r]:
                    return False

                l += 1
                r -= 1

            return True

        off = 1
        e = len(s)

        while e >= 1:
            for i in range(off):

                if pal(s, i, e + i - 1):
                    return s[i:e+i]

            e -= 1
            off += 1

        return ""