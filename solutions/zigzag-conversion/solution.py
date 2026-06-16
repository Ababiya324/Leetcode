class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        d=['']*len(s)
        i=0
        for j in range( len(s)):
            if (i==numRows-1):
                down=-1
            if(i==0):
                down=1

            d[i]+=s[j]
            i+=down
        return "".join(d)
        