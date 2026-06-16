class Solution(object):
    def addDigits(self, n):
        """
        :type num: int
        :rtype: int
        """
        c=0
        while n>9:
            c+=(n%10)
            n//=10
            if n<10:
                c=c+n
                n=c
                c=0
        return n

        