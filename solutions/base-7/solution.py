class Solution(object):
    def convertToBase7(self, nums):
        """
        :type num: int
        :rtype: str
        """
        o=''
        num=abs(nums)
        if nums==0:
            return '0'
        while num>0:
            
            o=str(num%7)+o
            num//=7
        return o if nums>=0 else '-'+o

        