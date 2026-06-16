class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        a={'1':'1','6':'9','8':'8','9':'6','0':'0'}
        for i in str(num):
            if i not in a:
                return False
        d=''
        for i in str(num):
            d=a[i]+d
        return d==str(num)

        