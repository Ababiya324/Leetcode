class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        d=0
        e=''
        if num==0:
                return '0'
        if num<0:
            num=(16 ** 8) + num
        while num>0:
                s=num%16
                if s>9:
                    e=chr(s+87)+e
                else:
                    e=str(s)+e
                num//=16
        
        return e
                


        