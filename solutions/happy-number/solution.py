class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        c=0
        d=set()
        while n>0:
                c+=((n%10)**2)
                n//=10
                if n==0: 
                    if c==1:
                        return True
                    if c in d:
                        return False
                    d.add(c)
                    n=c
                    c=0
            
        

        