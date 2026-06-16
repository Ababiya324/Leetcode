class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        c=''
        while n>0:
            c+=str(n%2)
            n//=2
        return not ('11' in c or '00' in c)
