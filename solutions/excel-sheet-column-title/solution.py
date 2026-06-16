class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        d=''
        while columnNumber>0:
            columnNumber-=1
            d=chr((columnNumber)%26+65)+d
            columnNumber//=26
        
        return d
