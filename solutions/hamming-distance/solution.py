class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        p=0
        while x>0 or y>0:
            if x%2+y%2==1:
                p+=1

            x//=2
            y//=2
        return p
            
        