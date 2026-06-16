class Solution(object):
    def findComplement(self, n):
        """
        :type num: int
        :rtype: int
        """
        c=0
        i=0
        while n>0:
            c+=(1-n%2)*2**i
            n//=2
            i+=1
        return c
        
        