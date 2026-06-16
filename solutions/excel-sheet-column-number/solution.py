class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        d=list(columnTitle)
        b=0
        for i in range(len(d)-1,-1,-1):
            b+=(ord(d[i])-64)*26**(len(d)-i-1)
        return b


        